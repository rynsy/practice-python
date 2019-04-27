#/usr/bin/python3
from itertools import product

def bcd(n):
    """
        Example:
            Input: 0b0011_0011      // 32 + 16 + 2 + 1 = 51

            Output: 0b0101_0001     // (5 * 10) + (1 * 1) = 51
                       |    |
                       5    1
    """
    global z_flag, c_flag, h_flag, n_flag 
    adjust = 0x60 if c_flag else 0x00
    if h_flag: adjust |= 0x06
    if not n_flag:
        if (n & 0x0f) > 0x09: adjust |= 0x06
        if (n > 0x99): adjust |= 0x60
        n = (n + adjust) & 0xff
    else:
        n = (n - adjust) & 0xff
    c_flag = adjust >= 0x60
    h_flag = False
    z_flag = n == 0
    return n

def test():
    for i in range(0xFF):
        print("i: {}".format(i))
        for c, h in product([True, False], repeat=2):
            c_flag, h_flag = c, h 
            print("\tC_FLAG={},H_FLAG={}:\n\t\tbin(i): {}\tbcd(i): {}".format(
                c_flag, h_flag, format(i, "#010b"), format(bcd(i), "#010b")))

if __name__ == "__main__":
    # Gameboy CPU Flags
    z_flag = False
    c_flag = False
    h_flag = False
    n_flag = False
    test()
