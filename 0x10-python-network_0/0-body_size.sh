#!/bin/bash

URL=$1

# Send a GET request to the provided URL and store the response in a temporary file
response=$(mktemp)
curl -s "$URL" -o $response

# Get the size of the response body
response_size=$(stat -c %s $response)
echo "Size of the response body: $response_size bytes"

# Clean up the temporary file
rm $response
