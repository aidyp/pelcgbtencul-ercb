module=/usr/local/lib/softhsm/libsofthsm2.so

pkcs11-tool --module $module --login -p 23456 --keypairgen --key-type rsa:4096 --label "rootaldrinkey" --id 1007 --usage-sign --slot 0x79b8e138

openssl req -out rootaldrincert.pem -nodes -key slot_2042159416-label_rootaldrinkey -keyform engine -config engine.conf -x509 -days 3650 -subj '/CN=ShopCA/C=GB/ST=Suffolk/L=Ipswich/O=Shop/OU=OnlineShop/' -sha256 -engine pkcs11

openssl req -new -newkey rsa:2048 -nodes -out interaldrin.csr -keyout interaldrin.pem -subj  '/CN=ShopCA/C=GB/ST=Suffolk/L=Ipswich/O=Shop/OU=OnlineShop/'

# OPENSSL_CONF=engine.conf openssl x509 -req -CAkeyform engine -engine pkcs11 -in interaldrin.pem -CA 
