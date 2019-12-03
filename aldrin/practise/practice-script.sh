module=/usr/local/lib/softhsm/libsofthsm2.so

pkcs11-tool --module $module --login -p 23456 --keypairgen --key-type rsa:4096 --label "rootaldrin.key" --id 1007 --usage-sign --slot 0x79b8e138

openssl req -out rootaldrincert.pem -nodes -key slot_2042159416-label_rootaldrin.key -keyform engine -config engine.conf -x509 -days 3650 -subj '/CN=rootCA/C=GB/ST=Suffolk/L=Ipswich/O=Shop/OU=OnlineShop/' -sha256 -engine pkcs11

pkcs11-tool --module $module --login -p 23456 --keypairgen --key-type rsa:2048 --label "interaldrin.key" --id 1009 --usage-sign --slot 0x79b8e138

openssl req -new -out interaldrin.csr -key slot_2042159416-label_interaldrin.key -keyform engine -engine pkcs11 -config engine.conf -subj '/CN=ShopCA/C=GB/ST=Suffolk/L=Ipswich/O=Shop/OU=OnlineShop/'

OPENSSL_CONF=inter-config.cnf openssl x509 -req -engine pkcs11 -in interaldrin.csr -out interaldrin.crt -days 1825 -CA rootaldrincert.pem -CAkey slot_2042159416-label_rootaldrin.key -CAcreateserial -extensions inter
