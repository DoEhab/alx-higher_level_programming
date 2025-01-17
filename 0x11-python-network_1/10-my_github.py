#!/usr/bin/python3
""" this module send post request with value to search for """
import requests
import sys


if __name__ == "__main__":
    """ post request """
    url = "https://api.github.com/user"
    name = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(name, password))
    if response.staus_code == 200:
        data = response.json()
        print("{}", data.get("id"))
    else:
        print("None")
