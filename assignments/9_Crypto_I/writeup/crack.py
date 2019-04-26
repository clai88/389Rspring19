#!/usr/bin/env python3

import hashlib
import string
import sys
import pdb

def crack():
    hashes = [line.strip() for line in open("hashes.txt", "r")] # open and read hashes.txt
    passwords = [line.strip() for line in open("passwords.txt", "r")] # open and read passwords.txt
    characters = string.ascii_lowercase

    d = {} 

    for c in characters:
        for p in passwords:
            full = c + p
            m = hashlib.sha256(full).hexdigest()
            d[m] = full
            # print("{}:{}".format(full,m))

            # print(p)
            # crack hashes
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

    pdb.set_trace()
    # iterate through hashes
    for h in hashes:
        if h in d:
            print("{}:{}".format(d[h],h))
        

if __name__ == "__main__":
    crack()
