#!/bin/bash

openssl genrsa -out root.key 4096 
openssl req -x509 -days 600 -key root.key -config config.cnf -out root.pem -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=rootcert"


openssl genrsa -out inter.key 2048
openssl req -new -key inter.key -config config.cnf -out inter.csr -sha256 -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=inter"

echo inter csr works

# openssl x509 -req -in inter.csr -out inter.pem -CA root.pem -CAkey root.key -CAcreateserial -days 300 -extfile config.cnf -extensions certificates
 openssl ca -config config.cnf -cert root.pem -in inter.csr -out inter.crt  -extensions certificates
# openssl verify -CAfile root.crt \ inter.crt# 
# openssl ca -gencrl -out CRL.pem -config config.cnf


# openssl genrsa -out end.key 2048
# openssl req -new -key end.key -config config.cnf -out end.csr -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=end"
# openssl ca -config config.cnf -keyfile inter.key -cert inter.cert -in end.csr -days 100 -out end.cert
