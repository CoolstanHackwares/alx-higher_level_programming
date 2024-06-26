#!/usr/bin/python3
"""A script that sends a POST request to a URL with an email address as a
parameter and displays the body of the response"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
