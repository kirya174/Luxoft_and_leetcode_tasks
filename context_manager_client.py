from connection import Connection


with Connection('localhost', 10000) as s:
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    s.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

print('closing socket')
