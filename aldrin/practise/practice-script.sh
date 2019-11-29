module=/usr/local/lib/softhsm/libsofthsm2.so
_config=/home/leslielamport/projects/openssl-pkcs11/aldrin/softhsm/engine.conf
_homedir=/home/leslielamport/projects/openssl-pkcs11/aldrin/softhsm

pkcs11-tool --module $module --login -p 23456 --keypairgen --key-type rsa:4096 --label "aldrinrootkey" --id 1007 --usage-sign --slot 0x79b8e138

openssl req -new -x509 -days 1825 -subj '/CN=subCA/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShop/OU=groceries/' -sha256 -config $_config -engine pkcs11 -keyform engine -key slot_2042159416-label_aldrinrootkey -out $_homedir"/aldrinrootcert.crt"
