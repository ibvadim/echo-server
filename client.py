#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address


while True:
    try:
        PORT = int(input('Select port from 1023 to 65535. Port = '))
        assert 1023 < PORT < 65535
    except ValueError:
        print("Not an integer! Please enter an integer.")
    except AssertionError:
        print("Please select PORT between 1023 and 65535")
    else:
        break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Connected to server ', HOST)
    while True:
        message = input()
        if message == 'exit':
            break

        s.sendall(bytes(message, 'utf-8'))
        print('Data sent')
        data = s.recv(1024)
        print('Data received: ', repr(data))

print('Disconnect from server')