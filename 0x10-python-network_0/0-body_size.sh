#!/bin/bash
# Displays the size of the body of the request
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
