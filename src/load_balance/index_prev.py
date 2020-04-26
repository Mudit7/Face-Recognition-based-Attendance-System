import sys,os,random
import simplejson
import requests
from sys import argv
import socket,socketserver
from requests_toolbelt.multipart import decoder
from http.server import BaseHTTPRequestHandler, HTTPServer

class basicRequestHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("index.html", "r")
        text = u"<h3>Application running at port: " + str(port) + "</h3>"
        self.wfile.write(text.encode(encoding='utf_8'))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        # Json upload
        print ("In post method Json contain")
        try:
            self.send_response(200)
            self.end_headers()
            data = simplejson.loads(self.data_string)
            print ("{}".format(data))
        except:
            print("No Json Object")
    
        #file upload
        print ("In post method File contain")
        
        print(self.data_string)
        # # testEnrollResponse = requests.post()
        # multipart_data = decoder.MultipartDecoder(self.data_string)

        # for part in multipart_data.parts:
        #     print(part.content)  # Alternatively, part.text if you want unicode
        #     print(part.headers)
        return


def run(server_class=HTTPServer, handler_class=basicRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":

    if len(argv) == 2:
        port = int(argv[1])
        print (f"Application is ready and listening to port {port}")
        run(port=int(argv[1]))
        
    else:
        run()
        print (f"Application is ready and listening to port {port}")
