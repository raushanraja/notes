### Let's Encrypt Cert generation and use
- On ubuntu 20.04 vm, given all the requirements are already installed
```base
    sudo apt update
    sudo apt-get install certbot  -y
    sudo certbot certonly --standalone
```
- The last command, when run for first time will ask for an email, and few other detail
- Then asks for domain, if no error occurs, then generated certs are saved in /etc/letsencrypt/live/GIVEN_DOMAIN/

### Small Python Scirpt to run a server and verify
- Save the file in `server.py`
- Run the file in terminal with `python3 server.py`
```python
import http.server
import socketserver
import ssl


######### MUST GIVE THE DOMAIN
DOMAIN="abc.com"


PORT = 8443  # Choose any available port
CERTIFICATE_FILE = f'/etc/letsencrypt/live/{DOMAIN}/cert.pem'  # Path to your SSL certificate
KEY_FILE = f'/etc/letsencrypt/live/{DOMAIN}/privkey.pem'  # Path to your SSL certificate

Handler = http.server.SimpleHTTPRequestHandler

# Create an SSL context with your certificate and private key
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile=CERTIFICATE_FILE, keyfile=KEY_FILE)

# Create the HTTPS server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
    print(f"Serving at https://localhost:{PORT}")
    httpd.serve_forever()
```
