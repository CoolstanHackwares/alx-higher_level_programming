#!/bin/bash
# A script that sends a request and displays the size of the response body using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
