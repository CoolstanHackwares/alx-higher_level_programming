#!/bin/bash
# Send POST request with file contents as JSON body and display response body
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
