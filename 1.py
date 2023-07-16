import http.server
import socketserver

PORT = 8000

class ImageHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/image':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')  # Замените на подходящий тип картинки
            self.end_headers()
            with open('/home/adryian/api-datasets/SRTM_BLR.tif', 'rb') as image_file:  # Замените на путь к вашей картинке
                self.wfile.write(image_file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

with socketserver.TCPServer(('', PORT), ImageHandler) as httpd:
    print(f'Serving at port {PORT}')
    httpd.serve_forever()
