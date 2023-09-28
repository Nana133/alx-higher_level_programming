#!/bin/bash
# Get the content-lenght of a giving ip address
curl -sI "$1" | awk '/Content-Length/{print $2}'
