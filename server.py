import sys
import BaseHTTPServer
import socket
import device

SERVER_IP = '0.0.0.0'
SERVER_PORT = 65000
CHECK_AV_DEVICES = 1
ADD_DEVICE = 1


devices = {}


def add_device():
    new_type = raw_input('Enter the type of the device : ')
    new_os = raw_input('Enter the type of the device : ')
    new_model = raw_input('Enter the model of the device : ')
    new_company = raw_input('Enter the company of the device : ')
    new_ip = raw_input('Enter the ip of the device : ')



def Edit_device():
    """
    The function will receive from the admin the param he want to edit in the deveice he want
    """

    device_to_edit = raw_input('Enter the device you want to edit : ')
    info_to_edit = raw_input('Enter info you want to edit : ')



server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))

server_socket.listen(1)

(client_socket, client_address) = server_socket.accept()
class DeviceManager:
    def add(self):
        pass
    def edit(self, device_name):
        pass
    def delete(self, device_name):
        pass
    def request_device(self, ):
        pass


class ServerRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print("hey")

class DistributeServer(BaseHTTPServer.HTTPServer):

    def __init__(self, server_address, handler_class=ServerRequestHandler):
        BaseHTTPServer.HTTPServer.__init__(self, server_address, handler_class)
        self.device_manager = DeviceManager()

if __name__ == "__main__":
    server = DistributeServer((SERVER_IP, SERVER_PORT))
    server.serve_forever()

while True:
    user = client_socket.recv(1024)
    if user == 'admin':
        client_socket.send('Choose option : 1)Add device 2)Edit Device 3)Remove user from device')
        option = client_socket.recv(1024)
        if option == ADD_DEVICE:
            pass

