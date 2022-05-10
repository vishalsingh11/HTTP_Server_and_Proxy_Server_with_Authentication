from http.server import HTTPServer , SimpleHTTPRequestHandler
import urllib.request
import base64

HOST = "127.0.0.2"
PORT = 8080

class MyProxyServer(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        username = "admin"
        password = "admin"
        self._auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(407)
        self.send_header("WWW-Authenticate", 'Basic realm="Test"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        url = self.path
        if self.headers.get("Proxy-Authorization") == None:
            self.do_AUTHHEAD()
            self.wfile.write(b"no auth header received")
        elif self.headers.get("Proxy-Authorization") == "Basic " + self._auth:
            self.send_response(200)
            self.send_header("Content-type" , "text/html")
            self.end_headers()
            self.copyfile(urllib.request.urlopen(url) , self.wfile)
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.get("Proxy-Authorization").encode())
            self.wfile.write(b"not authenticated")


server = HTTPServer( (HOST , PORT) , MyProxyServer)
server.serve_forever()
print("My Server has started ...")
server.serve_close()
print("My is closed now ...")