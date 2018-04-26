#!/usr/bin/env/python2

import pickle
import socket

addr = ("0.0.0.0", 9999)

# This function name doesn't lie
def code_exec():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(2)
    c_sock,c_addr = s.accept()
    tounpickle = c_sock.recv(1000)
    # Here is the serialization vuln
    pickle.load(tounpickle)
    c_sock.close()
    s.close()

while True:
    try:
        code_exec()
    except:
        pass

