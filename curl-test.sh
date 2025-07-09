#!/bin/bash

# POST request
echo "Posting new timeline post..."
curl.exe -X POST http://localhost:5000/api/timeline_post -d "name=TestUser&email=testuser@example.com&content=Hello from curl-test.sh!"

echo ""
echo "Retrieving all timeline posts..."
# GET request
curl.exe http://localhost:5000/api/timeline_post

echo ""
echo "Done!"
