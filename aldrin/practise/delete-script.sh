
rm *.pem *.csr 

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --delete-object --login -p 23456 --type privkey --slot 0x79b8e138 --id 1007

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --delete-object --login -p 23456 --type pubkey --slot 0x79b8e138  --id 1007
