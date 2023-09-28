#!/bin/bash
# This script displays all the allowed method by the server
curl -s -X "OPTIONS" "$1"
