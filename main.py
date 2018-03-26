from counter import *


def nprint(bits):
    ibin = bits2bin(bits)
    idec = int(ibin, 2)
    print(ibin, ':', idec)


def main():
    # 6 bits
    bits = [0, 0, 0, 0, 0, 0]
    nprint(bits)
    for _ in range(63):
        # Print out the bit count from 0 to 63 in order
        increment(bits)
        nprint(bits)
    for _ in range(63):
        # Print out the bit count from 63 to 0 in order
        nprint(bits)
        decrement(bits)
    nprint(bits)


if __name__ == '__main__':
    main()
