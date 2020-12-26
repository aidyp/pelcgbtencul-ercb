rm *.key *.csr *.srl *.cert *.crt *.pem index*

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 12345 --delete-object --type privkey --token-label "numero uno" --id 1007

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 12345 --delete-object --type pubkey --token-label "numero uno" --id 1007

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 12345 --delete-object --type privkey --slot 1135020572 --id 1008

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 12345 --delete-object --type pubkey --slot 1135020572 --id 1008

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 12345 --delete-object --type privkey --slot 968964284 --id 1009

pkcs11-tool --module /usr/local/lib/softhsm/libsofthsm2.so --login -p 12345 --delete-object --type pubkey --slot 968964284 --id 1009
