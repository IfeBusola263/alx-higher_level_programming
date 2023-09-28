#!/bin/bash
# This script sents a Post request and displays the body request
curl -s -X "POST" -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
