#!/usr/bin/env python3

import socket
import logging

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
logging.basicConfig(filename="serverlog.log", level=logging.INFO, format='%(asctime)s - %(message)s',)

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
    print('Server started')
    logging.info('Server started')
    s.bind((HOST, PORT))
    s.listen()
    logging.info('Start port listening')
    while True:
        conn, addr = s.accept()
        with conn:
            logging.info('Client connected: ', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                logging.info('Data received')
                conn.sendall(data)
                logging.info('Data sent')
        logging.info('Client disconnected: ', addr)
        logging.info('Start port listening')