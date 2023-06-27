from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(b"Hello World!")

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
