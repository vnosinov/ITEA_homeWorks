import datetime
import socket
import sys
from logging import getLogger, StreamHandler

logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 10002))
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
conn.settimeout(5)

with conn, sock:
    while True:
        data_received = conn.recv(1024)
        if data_received == b'':
            break
        with open('output.txt', 'a', encoding='utf-8') as f:
            print(f'{datetime.datetime.now()}: {data_received.decode("utf-8")}', file=f)
            logger.info(f'received data: {data_received}')
