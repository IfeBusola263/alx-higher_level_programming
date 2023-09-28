#!/bin/bash
# This script sends a url request and displays the size of the body
curl -s "$1" | wc -c
