#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (List[int]): A list of integers representing bytes of data

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get only the least significant 8 bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Check how many 1s are at the start of the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if num_bytes == 0:
                continue

            # If the number of bytes is more than 4 or less than 2
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # If this byte is not starting with 10, return False
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # We processed one byte
        num_bytes -= 1

    return num_bytes == 0
