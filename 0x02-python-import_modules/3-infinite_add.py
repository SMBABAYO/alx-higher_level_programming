#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    total = 0
    if length == 1:
        total = 0
    else:
        for x in range(1, length):
            total += int(sys.argv[x])
    print("{:d}".format(total))
