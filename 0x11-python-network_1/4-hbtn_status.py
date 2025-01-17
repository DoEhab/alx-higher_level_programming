#!/usr/bin/python3
""" this module fetch url reponse """
import requests


if __name__ == "__main__":
    """ print url response  """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

