#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
* You must use the package requests
* You are not allow to import packages other than requests
* The body of the response must be display like the following example
 (tabulation before -)
"""
import requests

if __name__ == "__main__":
    rq = requests.get("https://intranet.hbtn.io/status")
    text = rq.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
