#!/bin/bash
# Send POST request with file contents as JSON body and display response body
curl -sX POST -H "Content-Type: application/json" -d @"$file" "$url"
