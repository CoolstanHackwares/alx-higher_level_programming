#!/bin/bash
# Send request and extract status code using curl, without using pipe or redirection
curl -s -o /dev/null -w "%{http_code}" "$1"
