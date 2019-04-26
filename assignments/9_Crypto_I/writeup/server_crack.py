#!/usr/bin/env python3

import hashlib
import string
import socket
import time
import re
import pdb

def server_crack():
    hashes = [line.strip() for line in open("hashes.txt", "r")] # open and read hashes.txt
    passwords = [line.strip() for line in open("passwords.txt", "r")] # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    d = {}

    for c in characters:
        for p in passwords:
            full = c + p
            m = hashlib.sha256(full).hexdigest()
            d[m] = full

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    i = 0

    # crack 3 times
    while (i < 3):
        data = s.recv(1024)

        h = data.split("\n")[2]

        print(h)
        print(d[h])
        print("--------cracked hash--------------")
        s.send(d[h] + "\n")
        time.sleep(0.3)

        i += 1

    data = s.recv(1024)
    print("flag: {}".format(data))

if __name__ == "__main__":
    server_crack()
