
openssl req -new -newkey rsa:4096 -nodes -out shop.csr -keyout csrkey.pem -subj '/CN=subCA/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShop/OU=groceries/'
