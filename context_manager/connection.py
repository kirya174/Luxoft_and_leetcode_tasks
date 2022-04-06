import socket


class Connection:
    def __init__(self, address, port, is_server=False):
        self.sock = None
        self.server_address = (address, port)
        self.connection = None
        self.client_address = None
        self.is_server = is_server

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.is_server:
            print('starting up on {} port {}'.format(*self.server_address))
            self.sock.bind(self.server_address)
            self.sock.listen(1)
        else:
            print('connecting to {} port {}'.format(*self.server_address))
            self.sock.connect(self.server_address)
        return self.sock

    def __exit__(self, exc_type, value, trace):
        self.sock.close()