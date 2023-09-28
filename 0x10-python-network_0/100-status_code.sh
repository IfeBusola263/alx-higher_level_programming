#!/bin/bash
# This script sents a Post request and displays the body request
curl -s -w '%{http_code}' "$1"
