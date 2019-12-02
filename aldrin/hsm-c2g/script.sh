
openssl req -new -newkey rsa:2048 -nodes -out shop.csr -keyout csrkey.pem -subj '/CN=subCA/C=GB/ST=Suffolk/L=Ipswich/O=OnlineShop/OU=groceries/'
