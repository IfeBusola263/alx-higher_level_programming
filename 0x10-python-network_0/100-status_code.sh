#!/bin/bash
# This script sents a Post request and displays the body request
curl -s -L -w '%{response_code}' "$1"
