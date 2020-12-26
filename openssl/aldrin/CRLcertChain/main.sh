#!/bin/bash

##########prerequisites################
# mkdir serials
touch index.txt

##############root#############################

openssl genrsa -out root.key 4096 
openssl req -x509 -days 1000 -key root.key -config config.cnf -set_serial 2 -out root.pem -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=rootcert"

########################INTERMEDIATE#################################

openssl genrsa -out inter.key 2048
openssl req -new -key inter.key -config config.cnf -out inter.csr -sha256 -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=inter"

echo inter csr works

# openssl x509 -req -in inter.csr -out inter.pem -CA root.pem -CAkey root.key -CAcreateserial -days 300 -extfile config.cnf -extensions certificates
openssl ca -verbose -config config.cnf -name ca_default -days 500 -keyfile root.key -cert root.pem -in inter.csr -out inter.pem -batch -extfile config.cnf -extensions cert
# openssl verify -CAfile root.crt \ inter.crt#

###################CRL command##########################
openssl ca -gencrl -out CRL.pem -config config.cnf
echo beginning of endentity

##########################ENDENTITY#################
openssl genrsa -out end.key 2048
openssl req -new -key end.key -config config.cnf -out end.csr -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=end"
#openssl x509 -in end.csr -out end.pem -days 100 -CA inter.pem -CAkey inter.key -extfile config.cnf -extensions end
openssl ca -verbose -config config.cnf -days 100 -keyfile inter.key -cert inter.pem -in end.csr -out end.pem -batch -extfile config.cnf -extensions end
