# openssl req -new -newkey rsa:2048 -nodes -x509 -out rootaldrin.crt -keyout csrkey.pem -subj '/CN=subCA/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShop/OU=groceries/' -config config.cnf


# openssl req -new -newkey rsa:2048 -nodes -out interaldrin.csr -keyout csrkey.pem -subj '/CN=subCA/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShop/OU=groceries/' -config config.cnf

openssl req -new -newkey rsa:2048 -nodes -out end.csr -keyout end.key -subj '/CN=localhost/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShope/OU=groceries/'
openssl x509 -req -days 365 -in end.csr -out end.crt -CA interaldrin.crt -CAkey interaldrin.key -CAcreateserial -extfile end-config.cnf -extensions end_crt 


  
