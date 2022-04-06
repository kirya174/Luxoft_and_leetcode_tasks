from connection import Connection

with Connection('localhost', 10000, True) as s:
    while True:
        print('waiting for a connection')
        connection, client_address = s.accept()
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
