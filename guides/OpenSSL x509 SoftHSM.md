# OpenSSL x509 SoftHSM



## Overview

This guide tries to use x509 certificates with our softHSMv2. x509 is the certificate standard BT subscribes to



### Setup

I've already installed the pkcs11 engine to OpenSSL. You can check it here,

```bash
openssl engine -t -c pkcs11
```

As far as I understand, this is a generic pkcs11 engine, and just needs a pkcs11 interface to work.

As before, we set up an environment variable, `SOFTHSM` for the path to the pkcs11 library interface

```bash
export SOFTHSM=/usr/local/lib/softhsm/libsofthsm2.so
```



### OpenSSL Config File

You need to edit the openssl config file to tell it to use an engine. For this example, I've made a simpler config file that we point to, rather than add to the existing one:

```
openssl_conf = openssl_init

[openssl_init]
engines = engine_section

[engine_section]
pkcs11 = pkcs11_section

[pkcs11_section]
engine_id = pkcs11
#Dynamic path not needed because pkcs11 engine is already installed to openssl directory
#dynamic_path = /path/to/engine_pkcs11.so
MODULE_PATH = /usr/local/lib/softhsm/libsofthsm2.so
init = 0


#Regular openssl config commands go BELOW this engine header!

[ req ]
distinguished_name = req_dn
string_mask = utf8only
utf8 = yes

[ req_dn ]
commonName = Common Name (eg, your name)
```



### Generating A Key

In the last example, we generated a key using openSSL, and then *imported* it to the softHSM. This time, we're going to use `pkcs11-tool` to generate a key on-board the HSM.

```bash
sudo pkcs11-tool --module $SOFTHSM --login --pin 12345 --keypairgen --key-type rsa:2048 --label "509_key" --id 1001 --usage-sign
```



### Creating a Self-Signed Certificate

You can create a self signed certificate the normal way,

```bash
openssl req -new -x509 -days 365 -subj '/CN=test key/' -sha256 -config engine.conf -engine pkcs11 -keyform engine -key slot_748671277-label_509_key -out cert.pem
```

To find the number of the slot, you can use `sudo softhsm2-util --show-slots`. I'm not 100% sure how to preserve slot numbers across tries.

Inspecting the certificate using `openssl x509 -in cert.pem -text -noout` reveals a self-signed certificate, signed using the *private* key on the HSM.

*Note: Does a certificate have to be stored on HSM? I think it's okay, in theory the private key is the only important thing*



Now we have a "certificate authority", in the form of cert.pem



### Creating a Certificate Signing Request (CSR)

We want to use the CA (and it's corresponding private key) to sign a CSR. So first we make one in the normal style

```bash
openssl req -new -newkey rsa:2048 -nodes -out signmeplease.csr -keyout request.key
```



### Signing the CSR

I'm not an expert on CSRs and what to do with them, but I think it goes something like this

```bash
OPENSSL_CONF=engine.conf openssl x509 -req -CAkeyform engine -engine pkcs11 -in signmeplease.csr -CA cert.pem -CAkey slot_748671277-label_509_key -set_serial 1 -sha256 -out signed.pem

```

Note here the inclusion of `OPENSSL_CONF`. It looks like for `openssl x509 -req` instructions there is no `config` flag, so we just set the variable temporarily for the config file