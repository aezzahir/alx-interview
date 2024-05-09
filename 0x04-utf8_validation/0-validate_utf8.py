#!/usr/bin/python3
"""
0x04. UTF-8 Validation
0x04. UTF-8 Validation
0x04. UTF-8 Validation
0x04. UTF-8 Validation
"""


def check_bytes(num):
    """
    Returns how many bytes needed to represent num in UTF-8 encoding
    """
    base = 1 << 7
    count = 0
    while base & num:
        count += 1
        base >>= 1
    return count


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    count = 0
    for item in data:
        if count == 0:
            count = check_bytes(item)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            if check_bytes(item) != 1:
                return False
            count -= 1
    if count == 0:
        return True
    return False
