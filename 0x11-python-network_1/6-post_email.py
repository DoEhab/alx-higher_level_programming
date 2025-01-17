#!/usr/bin/python3
""" this module send post request with email value """
import requests
import sys


if __name__ == "__main__":
    """ print url response header X-Request-Id """
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    content = requests.post(url, data=data)
    print(content.text)

