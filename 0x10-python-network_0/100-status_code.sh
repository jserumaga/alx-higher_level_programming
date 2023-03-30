#!/bin/bash
#
curl -s -o /dev/null -sIw "%{http_code}" "$1"
