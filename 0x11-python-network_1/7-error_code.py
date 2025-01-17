#!/usr/bin/python3
""" this module send post request and print the error code """
import requests
import sys


if __name__ == "__main__":
    """ print url response error """
    url = sys.argv[1]
    response = requests.post(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

