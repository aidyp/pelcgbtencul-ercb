#!/bin/bash

module=/usr/local/lib/softhsm/libsofthsm2.so
config=configSofthsm.cnf
label1=key-1
label2=key-2
label3=key-3
slot1=1593683345
slot2=1135020572
slot3=968964284



##########prerequisites################
# mkdir serials
touch index.txt

##############ROOT#############################

# ~/projects/openssl-pkcs11/engine/jakes_stuff$

pkcs11-tool --module $module --login -p 12345 --keypairgen --key-type rsa:4096 --label $label1 --id 1007 --slot $slot1 --usage-sign

openssl req -out root.pem -new -nodes -key slot_$slot1-label_$label1 -keyform engine -config $config -x509 -days 1000 -extensions cert -reqexts csr_extensions -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Company/OU=test/CN=root" -verbose -engine pkcs11


#openssl genrsa -out root.key 4096 
#openssl req -x509 -days 1000 -key root.key -config config.cnf -set_serial 2 -out root.pem -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=rootcert"

########################INTERMEDIATE#################################

pkcs11-tool --module $module --login -p 12345 --keypairgen --key-type rsa:2048 --label $label2 --id 1008 --slot $slot2 --usage-sign

openssl req -new -key slot_$slot2-label_$label2 -keyform engine -config $config -out inter.csr -sha256 -reqexts csr_extensions -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=inter" -verbose -engine pkcs11

openssl ca -verbose -config $config -days 500 -keyfile slot_$slot1-label_$label1 -keyform engine -cert root.pem -in inter.csr -out inter.pem -batch -extfile $config -extensions cert -engine pkcs11


#openssl genrsa -out inter.key 2048
#openssl req -new -key inter.key -config config.cnf -out inter.csr -sha256 -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=inter"
#echo inter csr works
#openssl ca -verbose -config config.cnf -name ca_default -days 500 -keyfile root.key -cert root.pem -in inter.csr -out inter.pem -batch -extfile config.cnf -extensions cert

###################CRL command##########################
openssl ca -gencrl -out CRL.pem -keyfile slot_$slot2-label_$label2 -config $config -engine pkcs11 -keyform engine
#echo beginning of endentity

##########################ENDENTITY#################

pkcs11-tool --module $module --login -p 12345 --keypairgen --key-type rsa:2048 --label $label3 --id 1009 --slot $slot3 --usage-sign

openssl req -new -key slot_$slot3-label_$label3 -keyform engine -config $config -out end.csr -sha256 -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=endentity" -verbose -engine pkcs11

openssl ca -verbose -config $config -days 365 -in end.csr -out end.pem -keyfile slot_$slot2-label_$label2 -keyform engine -batch -extfile $config -extensions end -engine pkcs11


#openssl genrsa -out end.key 2048
#openssl req -new -key end.key -config config.cnf -out end.csr -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=end"
#openssl x509 -in end.csr -out end.pem -days 100 -CA inter.pem -CAkey inter.key -extfile config.cnf -extensions end
#openssl ca -verbose -config config.cnf -days 100 -keyfile inter.key -cert inter.pem -in end.csr -out end.pem -batch -extfile config.cnf -extensions end
