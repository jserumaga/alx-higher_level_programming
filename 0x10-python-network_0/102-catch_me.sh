#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing in the body of the response
curl 0.0.0.0:5000/catch_me -sLX PUT -d "user_id=98" -H "You got me!"
