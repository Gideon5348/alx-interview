#!/usr/bin/python3
"""
A method that determines if a given data set reps a valid UTF-8 encoding."""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    data : List[int]
        A list of integers representing bytes of data.

    Returns:
    bool
        True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        if byte > 255:
            return False

        binary_repr = format(byte, '08b')

        if num_bytes == 0:
            if binary_repr[0] == '0':
                continue
            elif binary_repr[:3] == '110':
                num_bytes = 1
            elif binary_repr[:4] == '1110':
                num_bytes = 2
            elif binary_repr[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            if binary_repr[:2] != '10':
                return False
            num_bytes -= 1

    return num_bytes == 0
