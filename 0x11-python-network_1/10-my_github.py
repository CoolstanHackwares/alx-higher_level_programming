#!/usr/bin/python3
"""A script that takes GitHub creds and the GitHub API to display your id"""
import sys
import requests


def get_github_id(username, password):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json()["id"]
    else:
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)
