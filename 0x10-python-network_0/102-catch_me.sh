#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"
curl -sX PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "Origin: HolbertonSchool"
