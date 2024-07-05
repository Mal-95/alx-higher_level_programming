#!/bin/bash
# Send the POST request and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$FILE" "$URL"
