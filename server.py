from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import device_manager
import json

SERVER_IP = 'localhost'
SERVER_PORT = 8000


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        if self.path == '/api/get_devices':
            devices = self.server.dev_manager.get_all_devices()
            print type(devices), "devices"
            json_devices = json.dumps(devices, encoding="utf-8")
            print json_devices, "do get"
            self.wfile.write(json_devices)

    def do_POST(self):

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        if self.path == '/api/add_device':
            content_length = int(self.headers['Content-Length'])
            raw_data = self.rfile.read(content_length)
            json_data = json.loads(raw_data)
            print json_data
            self.server.dev_manager.add_device(json_data)

        elif self.path == '/api/occupy_device':
            content_length = int(self.headers['Content-Length'])
            raw_data = self.rfile.read(content_length)
            json_data = json.loads(raw_data)
            print json_data
            self.server.dev_manager.occupy_dev(raw_data)


class MyServer(HTTPServer):
    def __init__(self, host, port):
        HTTPServer.__init__(self, (host, port), MyHandler)
        self.dev_manager = device_manager.DeviceManager()


def main():
    server = MyServer(SERVER_IP, SERVER_PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()