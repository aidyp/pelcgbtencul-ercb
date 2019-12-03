
rm *.pem *.csr *.srl *.crt  

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 23456 --delete-object --type privkey --id 1007

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --delete-object --login -p 23456 --type pubkey  --id 1007

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 23456 --delete-object --type pubkey --id 1009

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 23456 --delete-object --type privkey --id 1009
