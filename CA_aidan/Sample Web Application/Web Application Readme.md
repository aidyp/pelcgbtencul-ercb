# Web Application Readme



### Signing for a web application

#### Installation

We want to make sure that we can verify correct certificates, and reject incorrect certificates. For that end, we need an end-point application. As a skeleton, we're going to use a basic `nginx` server, and configure it to handle SSL connections

```bash
apt install -y nginx
systemctl start nginx
```

Edit the default configuration file found at `/etc/nginx/sites-available/default` to allow for SSL connections:

```
server {
	... 
	listen 443 ssl default_server;
	listen [::]:443 ssl default_server;
	
	ssl_certificate     /PATH/TO/CRT;
	ssl_certificate_key /PATH/TO/KEY;
}
```

If you want to use a `.cert` file, then use that file for both `ssl_certificate` and `ssl_certificate_key`

You can visit the website by typing `localhost` into your browser. To try the TLS version, go to `https://localhost`. It won't work now, because we haven't configured the certificates.



#### Root CA

We don't want to use self-signed certificates, or create a local CA. Our aim is to have a working certificate chain, where trust is derived from a root that we specify.

As a result, you will need to install the root certificate onto the browser you use to visit