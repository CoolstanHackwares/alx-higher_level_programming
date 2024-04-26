#!/usr/bin/python3
"""A script that Sends a POST request to http://0.0.0.0:5000/search_user"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
