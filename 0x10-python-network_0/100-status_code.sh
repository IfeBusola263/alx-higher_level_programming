#!/bin/bash
# This script sents a Post request and displays the body request
curl -sIL -w '%{response_code}' "$1"
