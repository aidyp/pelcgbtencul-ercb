# Server Configurations

The following must be written inside the `server{}` bracket within the Nginx config file which will be found in `/etc/nginx/sites-available/`

#### Enable HTTPS

To enable HTTPS instead of just HTTP, open port 443

`listen 443 ssl default_server;`

``listen [::]:443 ssl default_server;`

#### Add Domain Name

Add the domain name that you will connect to e.g. `localhost` for https://localhost. This domain name must be the same as the common name of your end-entity certificate for a secure connection.

`server_name localhost;`

#### Add certificate bundle and key

Add the path to the private key of the end-entity certificate.

`ssl_certificate_key /home/leslielamport/projects/openssl-pkcs11/aldrin/hsm-c2g/end.key;`

Lastly add the path to the bundle of the end-entity and intermediate certificate, with end-entity certificate first, followed by the intermediate certificate. This bundle should be saved as a .pem file.

`ssl_certificate /home/leslielamport/projects/openssl-pkcs11/aldrin/hsm-c2g/bundle.pem;`