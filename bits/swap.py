import sys

if len(sys.argv) < 3:
    print("Expected ./swap.py [A] [B]")

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("A: {}\tB: {}".format(a,b))
    print("Swapping...")
    a ^= b
    b ^= a
    a ^= b
    print("A: {}\tB: {}".format(a,b))
