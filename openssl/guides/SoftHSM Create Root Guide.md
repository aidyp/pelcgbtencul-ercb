## Creating Root Private Key on HSM

The aim is to create the root private key on the HSM using PKCS11-Tool and then use an OpenSSL command on the HSM in order to create a certificate using the private key stored on the HSM without ever having access to the private key.

Script to do this found at: `/home/leslielamport/Documents/Github/openssl-pkcs11/hsm_work/cert_hsm.sh` - this script needs to be run as `sudo`.



#### Creating the Root Private Key on the HSM:

```bash
sudo pkcs11-tool --module $_module --login --pin 12345 --keypairgen --key-type rsa:4096 --label "root_key" --id $_keyid --usage-sign
```

The command is using the libsofthsm2.so module found at: `_module=/usr/local/lib/softhsm/libsofthsm2.so`

It is logging into the HSM using the `--pin` (for testing at the moment, will remove this option for security eventually), then generating a keypair of type RSA with a bit length of 4096 and giving it a `--label` of "root_key", giving it an ID specified by the user in the script, and telling the key it will be used for signing.



#### Creating a Local Certificate using the Root Private Key on the HSM:

```bash
sudo openssl req -out $_homedir"/"$_rootname".crt" -new -nodes -engine pkcs11 -keyform engine -key slot_748671277-label_root_key -config $_config_file -days 9125 -extensions root_cert -reqexts v3_req -x509 -subj "/C=GB/ST=Essex/L=Ipswich/O=BT PLC/OU=test/CN=jake test root"
```

This command is creating a certificate by connecting to the HSM using the engine pkcs11 and using the private key from the slot `748671277` with the label `root_key` using the config specified in the script, setting the days to 9125 (7 years), using the extension block `root_cert` from the config, use another extension block called `v3_req` from the config, make an x509 certificate, and set the subject parameters.