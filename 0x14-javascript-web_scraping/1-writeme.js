#!/usr/bin/node
// import the file system module
const fs = require('fs');

// Open the file for writing
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
