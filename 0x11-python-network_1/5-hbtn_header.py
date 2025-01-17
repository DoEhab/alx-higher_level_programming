#!/usr/bin/python3
""" this module send post request to the passed url """
import requests
import sys


if __name__ == "__main__":
    """ print url response header X-Request-Id """
    url = sys.argv[1]
    content = requests.get(url)
    print(content.headers.get("X-Request-Id"))
