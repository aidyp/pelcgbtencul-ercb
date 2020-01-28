#!/bin/bash

openssl genrsa -out root.key 4096 
openssl req -x509 -days 600 -key root.key -config config.cnf -out root.crt -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=rootcert"


openssl genrsa -out inter.key 2048
openssl req -new -key inter.key -config config.cnf -out inter.csr -sha256 -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=inter"

# openssl x509 -in inter.csr -out inter.cert -CA root.cert -CAkey root.key -days 300 -extfile config.cnf
openssl ca -config config.cnf -keyfile root.key -days 300 -cert root.crt -in inter.csr -out inter.crt  -extensions certificates -extfile config.cnf
# openssl ca -gencrl -out CRL.pem -config config.cnf


# openssl genrsa -out end.key 2048
# openssl req -new -key end.key -config config.cnf -out end.csr -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Security/OU=team1/CN=end"
# openssl ca -config config.cnf -keyfile inter.key -cert inter.cert -in end.csr -days 100 -out end.cert
