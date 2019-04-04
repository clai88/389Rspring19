#!/usr/bin/env python3

import sys
from struct import pack, unpack
import time
import base64


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

offset = 24
for i in range(section):
    stype, slen = unpack("<LL", data[offset:offset + 8])

    print("Section Type: {}".format(stype))
    print("Section Length: {}".format(slen))

    offset += 8

    # SECTION_ASCII (0x1)
    if stype == 1:
        (message,) = unpack("<{}s".format(slen), data[offset:offset + slen])

        if message[-1] == "=":
            message = base64.b64decode(message)
            print("ASCII: {}".format(message))
        else:
            print("ASCII: {}".format(message))

    # SECTION_UTF8 (0x2) -- UTF-8-encoded text.
    if stype == 2:
        (message,) = unpack("<{}s".format(slen), data[offset:offset + slen])
        print("UTF-8: {}".format(message))

    # SECTION_WORDS (0x3) -- Array of words.
    if stype == 3:
        (message,) = unpack("<{}s".format(slen/4), data[offset:offset + slen/4])
        print("WORDS: {}".format(message))

    # SECTION_DWORDS (0x4) -- Array of dwords.
    if stype == 4:
        for i in range(0, slen, 8):
            (message, ) = unpack("<8s", data[offset + i, offset + i + 8])
            print("DWORDS: {}".format(message))

    # SECTION_DOUBLES (0x5) -- Array of doubles.
    if stype == 5:
         for i in range(0, slen, 8):
            (message, ) = unpack("<8s", data[offset + i, offset + i + 8])
            print("DOUBLES: {}".format(message))

    # SECTION_COORD (0x6) -- (Latitude, longitude) tuple of doubles.
    if stype == 6:
        if slen == 16:
            (latitude, longitude) = unpack("<dd", data[offset:offset + slen])
            print("Coordinates: ({}, {})".format(latitude, longitude))
        else:
            print("Wrong length, expected 16, got {}".format(slen))

    # SECTION_REFERENCE (0x7) -- The index of another section.
    if stype == 7:
        (message,) = unpack("<d", data[offset:offset+slen])
        print("REFERENCE: {}".format(message))

    # SECTION_PNG (0x8) -- Embedded PNG image.
    if stype == 8:
        header = b"\x89\x50\x4E\x47\x0d\x0a\x1a\x0a"
        with open("embedded_png.png", "wb") as f:
            f.write(header)
            f.write(data[offset:offset + slen])

        print("PNG saved to embedded_png.png")

    # SECTION_GIF87 (0x9) -- Embedded GIF87.
    if stype == 9:
        header = b"\x47\x49\x46\x38\x37\x61"
        with open("embedded_gif87.png", "wb") as f:
            f.write(header)
            f.write(data[offset:offset + slen])
        
        print("GIF87 saved to embedded_gif87.png")

    # SECTION_GIF89 (0xA) -- Embedded GIF89.
    if stype == 10:
        header = b"\x47\x49\x46\x38\x39\x61"
        with open("embedded_gif89.png", "wb") as f:
            f.write(header)
            f.write(data[offset:offset + slen])

        print("GIF89 saved to embedded_gif89.png")

    offset += slen

