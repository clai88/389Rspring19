#!/bin/sh
dd conv=notrunc if=ecb.bmp of=test_ecb.bmp bs=54 count=1
dd conv=notrunc if=cbc.bmp of=test_cbc.bmp bs=54 count=1
