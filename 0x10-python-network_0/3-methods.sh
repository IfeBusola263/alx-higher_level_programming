#!/bin/bash
# This script displays all the allowed method by the server
curl -s -I -X "OPTIONS" "$1" | grep "ALLOW" | cut -d ":" -f 2
