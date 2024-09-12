#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0
    arg_len = len(sys.argv)
    for i in range(arg_len - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
