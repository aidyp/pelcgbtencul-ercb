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

Remember that the `ssl_certificate_key` is the server's **private** key -- it will need to know where it is for the SSL Connection.

You can visit the website by typing `localhost` into your browser. To try the TLS version, go to `https://localhost`. It won't work now, because we haven't configured the certificates.



#### Adding The Certificates

Point `ssl_certificate` and `ssl_certificate_key` configuration options to the certificate *bundle*.

The bundle can be constructed like this:

```bash
cat end_certificate.crt intermediate_crt.crt root_crt.crt > end_certificate.chained.crt
```

So your final config will look like:

```
server {
	...
	listen 443 ssl default_server;
	listen [::]:443 ssl_default_server;
	
	ssl_certificate /path/to/end_certificate.chained.crt;
	ssl_certificate_key /path/to/end_certificate_key.key;
}
```



You can check the chain is properly displayed by connecting using the OpenSSL `s_client` utility,

```bash
openssl s_client -connect localhost:443
```

Which will display the chain and attempt to make an SSL connection to the server. At the moment, it won't return cleanly.

That's something we need to get sorted.

#### Root CA

We don't want to use self-signed certificates, or create a local CA. Our aim is to have a working certificate chain, where trust is derived from a root that we specify.

As a result, you will need to install the root certificate onto the browser you use to visit