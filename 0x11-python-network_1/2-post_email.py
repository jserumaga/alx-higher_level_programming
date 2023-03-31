#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the header
    of the response.
    * You must use the packages urllib and sys
    * You are not allow to import packages other than urllib and sys
    * The value of this variable is different for each request
    * You don’t need to check arguments passed to the script (number or type)
    * You must use a with statement
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
