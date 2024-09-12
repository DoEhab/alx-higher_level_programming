#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    module_data = dir(hidden_4)
    for data in module_data:
        if data[0:2] != "__":
            print(data)


