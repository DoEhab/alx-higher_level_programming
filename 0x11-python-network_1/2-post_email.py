#!/usr/bin/python3
""" this module send post request to the passed url """
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    """ print url response header X-Request-Id """
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
