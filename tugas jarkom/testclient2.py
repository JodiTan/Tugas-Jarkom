# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:03:27 2020

@author: jodit
"""

import socket


def main(ip, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        print('Sending to server...')
        sock.send('hello, world!'.encode('UTF-8'))

    print('stopped')


if __name__ == '__main__':

    main('127.0.0.1', 5005)