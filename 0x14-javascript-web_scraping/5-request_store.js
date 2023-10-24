#!/usr/bin/node
// import the required module - request and file system(fs)
const request = require('request');
const fs = require('fs');

// Make the request and save the response in a file
request(process.argv[2], 'utf8').pipe(fs.createWriteStream(process.argv[3]));
