def increment(bits):
    # Increment the bit counter by 1
    i = 0
    m = len(bits) - 1
    while i <= m and bits[m-i] == 1:
        bits[m-i] = 0
        i += 1
    # Index overflow prevention
    if i <= m:
        bits[m-i] = 1


def decrement(bits):
    # Decrement the bit counter by 1
    i = 0
    m = len(bits) - 1
    while i <= m and bits[m-i] == 0:
        bits[m-i] = 1
        i += 1
    # Index overflow prevention
    if i <= m:
        bits[m-i] = 0


def bits2bin(bits):
    return ''.join([str(b) for b in bits])