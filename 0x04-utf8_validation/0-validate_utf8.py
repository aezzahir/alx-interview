#!/usr/bin/python3
"""
0x04. UTF-8 Validation
"""


def validUTF8(data):
    n_bytes = 0
    for byte in data:
        byte_bin = bin(byte)[2:].zfill(8)
        if n_bytes == 0:
            if byte_bin[0] == '0':
                continue
            elif byte_bin[:3] == '110':
                n_bytes = 2
            elif byte_bin[:4] == '1110':
                n_bytes = 3
            elif byte_bin[:5] == '11110':
                n_bytes = 4
            else:
                return False
            n_bytes -= 1
        else:
            if not byte_bin.startswith('10'):
                return False
            n_bytes -= 1
    return n_bytes == 0
