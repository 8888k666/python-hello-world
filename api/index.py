from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(bytes(self.client_address[0].encode('utf-8')))
        # self.wfile.write('Hello, world!'.encode('utf-8'))
        return
