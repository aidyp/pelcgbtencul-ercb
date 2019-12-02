
#openssl req -new -newkey rsa:2048 -x509 -out test.crt -keyout test.key -days 2434 -nodes -config aidan_ca_openssl.cnf

openssl genrsa -out test.key 2048
openssl req -out test.crt -x509 -new -nodes -key test.key -config aidan_ca_openssl.cnf -days 3424 
