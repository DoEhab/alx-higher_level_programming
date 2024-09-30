#!/usr/bin/python3
def safe_print_list(my_list, x):
    result = ""
    for i in range(x):
        try:
            result += str(my_list[i])
        except IndexError:
            print("Index Out of Range")
    result += '\n'
    return int(result)

