
# openssl req -new -newkey rsa:2048 -nodes -out shop.csr -keyout csrkey.pem -subj '/CN=subCA/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShop/OU=groceries/'

 openssl req -new -newkey rsa:2048 -nodes -out end.csr -keyout end.key -subj '/CN=endentity/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShope/OU=groceries/'
 openssl x509 -req -days 365 -in end.csr -out end.crt -CA inter.crt -CAkey csrkey.pem -CAcreateserial -extfile config -extensions end  

openssl rsa -in end.key -pubout -out endpub.key
