import socket
import sys
from logging import getLogger, StreamHandler
from time import sleep

logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")


sock = socket.create_connection(('127.0.0.1', 10002), timeout=5)
sock.settimeout(2)

with sock:
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            data_send = line.strip('\n').encode('utf-8')
            sock.sendall(data_send)
            logger.info(f'send data: {data_send}')
            sleep(0.5)
