from http.server import HTTPServer , SimpleHTTPRequestHandler

HOST = "127.0.0.3"
PORT = 8080

class MyServer(SimpleHTTPRequestHandler):

    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type" , "text/html")
        self.end_headers()
        # use below line if intention is to list files in current directory
        #SimpleHTTPRequestHandler.do_GET(self)
        # otherwise use below approach to display text
        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>" , "utf-8"))

server = HTTPServer( (HOST , PORT) , MyServer)
server.serve_forever()
print("My Server has started ...")
server.serve_close()
print("My is closed now ...")