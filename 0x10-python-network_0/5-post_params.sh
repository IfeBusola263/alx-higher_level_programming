#!/bin/bash
# This script sents a Post request and displays the body request
curl -s -X "POST" -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
