#!/usr/bin/python3
"""Sends a POST request to a URL with an email as a parameter and displays
the body of the response"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    try:
        with urllib.request.urlopen(url, data=data) as response:
            print("Your email is: {}".format(email))
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
