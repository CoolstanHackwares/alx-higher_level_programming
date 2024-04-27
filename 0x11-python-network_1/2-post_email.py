#!/usr/bin/python3
"""Sends a POST request to a URL with an email as a parameter and displays
the body of the response"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
