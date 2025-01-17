#!/usr/bin/python3
""" this module print url reponse  header X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    """ print url response header X-Request-Id """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers
        print(header.get('X-Request-Id'))

