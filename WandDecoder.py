#!/usr/bin/env python
# -*- coding: utf-8 -*-
from struct import unpack
from hashlib import md5
import pyDes

#Explanation for decrypting process: http://securityxploded.com/operapasswordsecrets.php
#They mention that the original reverse engineering was done by sna@reteam.org, but I could find no evidence of that on reteam.org

salt="0x83, 0x7D, 0xFC, 0x0F, 0x8E, 0xB3, 0xE8, 0x69, 0x73, 0xAF, 0xFF".replace("0x", "").replace(", ", "").decode("hex")

def decode_block(file):
    # get past obfuscation:
    salted_key = file.read(8)
    data_size = unpack('>i', file.read(4))[0]
    if data_size % 8 > 0: #data must be in blocks of 8 byte for DES, sometimes it is not
        print("Skipped data block of size " + str(data_size))
        return
    encrypted_data = file.read(data_size)
    md51 = md5(salt + salted_key).digest()
    md52 = md5(md51 + salt + salted_key).digest()
    #decrypt data block:
    data = pyDes.triple_des(md51+md52[:8], pyDes.CBC, md52[8:]).decrypt(encrypted_data)
    #clean up data:
    endpos = data.find("0000".decode("hex"))
    if endpos != -1:
        if endpos % 2 == 1:
            endpos += 1
        data = data[:endpos]
    data = data.decode("utf-16")
    data = data.rstrip(u"ࠈ؆Ȃ")
    #print data
    print(data.encode("utf-8"))

def decode_file(file_path):
    with open(file_path, "rb") as file:
        while True:
            # find an int of 4 bytes with value of 8 which marks the start of a block
            s = "xxxx"
            g = "00000008".decode("hex")
            while s != g:
                s = s[1:] + file.read(1)
                if len(s) != 4:
                    return
            decode_block(file)

from sys import argv

filename = "../wand1.dat"
if len(argv) > 1:
    filename = argv[1]
decode_file(filename)
