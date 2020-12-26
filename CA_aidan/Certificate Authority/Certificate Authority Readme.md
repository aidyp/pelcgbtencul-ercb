# Certificate Authority Readme



This directory contains a Certificate Authority that wants to sign certificates for applications in its domain. 

This CA wants to get its authority from a root CA (Jake)





### Generating A Key

Certificate Authority keys should be 2048 bits in length, and use SHA-256 hashes for the certificates

##### Keygen

Key generation is not tricky. We can use `pkcs11-tool`.

```
export HSM_MODULE=/usr/local/lib/softhsm/libsofthsm2.so
export SLOT_ID= [Slot ID of desired token]
pkcs11-tool --module $HSM_MODULE --login --slot $SLOT_ID --keypairgen --key-type rsa:2048 --usage-sign --label "CA_key" --id 0001
```

For the softHSM on my machine, the slot ID is `107282534`. Yours will likely differ



### Generate A CSR

Our CA wants to generate a Certificate Signing Request (that it sends to our root CA).  Recall, normally the command is:

```bash
openssl req -new -x509 -key privatekey.key -out request.csr
```

If you've used an HSM, you want to generate the request on-board the HSM. For an exact guide, see `guides/OpenSSL x509 SoftHSM`. We also need to change the config file to allow it. An example one is included in the same directory as this guide as `aidan_ca_openssl.cnf`

```bash
openssl req -new -x509 -days 365 -sha256 -config [ssl config file].conf -engine pkcs11 -keyform engine -key slot_[slot num]-label_[keylabel] -out request.csr
```

### 