#!/bin/bash
# This script sents a Post request and displays the body request, with the content of a file
curl -s -X "POST" -d @"$2" "$1"
