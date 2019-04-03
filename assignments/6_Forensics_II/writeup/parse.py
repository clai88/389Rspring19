#!/usr/bin/env python3

import sys
from struct import pack, unpack
import time


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8badf00d
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = unpack("<LL", data[0:8])
(timestamp,) = unpack("<L", data[8:12])
(author,) = unpack("<8s", data[12:20])
(section,) = unpack("<L", data[20:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

time_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

print("------- HEADER -------")
print("MAGIC: {}".format(hex(magic)))
print("VERSION: {}".format(int(version)))

print("TIMESTAMP: {} ({})".format(timestamp, time_datetime))
print("AUTHOR: {}".format(author))
print("SECTION: {}".format(section))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

