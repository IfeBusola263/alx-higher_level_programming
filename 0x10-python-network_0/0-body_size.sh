#!/bin/bash
# This script sends a url request and displays the size of the body
curl -sw '%{size_download}\n' "$1"
