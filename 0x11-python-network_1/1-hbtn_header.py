#!/usr/bin/python3
import urllib.request
import sys
""" print url response header X-Request-Id"""
if __name__ == "__main__":
    """ print url response header X-Request-Id """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers
        print(header.get('X-Request-Id'))
