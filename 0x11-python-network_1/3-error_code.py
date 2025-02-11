#!/usr/bin/python3
""" this module print url reponse  header X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    """ print url response header X-Request-Id """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
