# OpenSSL & SoftHSM

The aim of this directory is to explore using our software HSM (softHSMv2) with OpenSSL. In this document I'm just trying to write down some stuff so I don't have to keep reminding myself of it.

The sample workflow here is to load a key into the softHSM first, then try to get OpenSSL to use it to do some signing work.



### Initialising Tokens

The softHSM requires root access, so use `sudo` when running these commands.

```bash
sudo softhsm-util --init-token --label "Token-1" --token "Token-1"
```

Initialises the token I've already created on the softHSM.

### Environment Variables

In Unix, you can set *environment* variables instead of having to type out directories every time. This is useful for us. HSMs really are usually just a library file that you send commands into and get results out of. In our example, the softhsm libraries are here: `/usr/local/lib/softhsm`. 

To create an environment variable,

```bash
export SOFTHSM=/usr/local/lib/softhsm/libsofthsm2.so
```

To access an environment variable, use the `$` sign,

```bash
echo $SOFTHSM
/usr/local/lib/libsofthsm2.so
```



### Generating a Key via OpenSSL

Ideally you'd generate the key on the HSM, but baby steps I think. Especially as this might be a feature we need to learn and practice in the future.

Here's how to create a normal public/private keypair, wrapping it as a `.pem`

```bash
openssl genrsa -nodes -out private.pem 1024
openssl rsa -in private.pem -outform PEM -pubout public.pem
```

PKCS#8 specifies the format that private certificate keypairs are transferred in, so you need to tell openSSL to convert it to PKCS#8

```bash
openssl pkcs8 -topk8 -inform PEM -outform PEM -in private.pem -out pkcs8private.pem.pkcs8 -nocrypt
```

You can check it worked by looking at it again:

```bash
openssl pkey -in pkcs8private.pem.pkcs8 -text
```



### Importing Key into SoftHSMv2

Now that we have a key, we want to import it into the softHSMv2

```bash
softhsm2-util --import pkcs8private.pem.pkcs8 --label "rsa key" -id 1111 --token "Token-1"
```

You can view the key on the software HSM by using `pkcs11-tool` [Can also write our own using the python pkcs11 interface -- a project for another time perhaps]

```bash
sudo pkcs11-tool --module $SOFTHSM --list-objects
```



### Signatures

The private key is on the softHSM. We want to sign some data with it, and verify that it was signed.

```bash
#Make some test data to sign
echo "It's your time to sign" > data
#Sign the data on the HSM using the private key
sudo pkcs11-tool --token-label "Token-1"--id 1111 -s -p 12345 -m RSA-PKCS --module SOFTHSM --input-file data --output-file data.sig
#Now we just use the OpenSSL verify feature, with the public key we already have
sudo openssl rsautl -verify -inkey public.pem -in data.sig -pubin
#And we should get the result: "It's your time to sign"
```

