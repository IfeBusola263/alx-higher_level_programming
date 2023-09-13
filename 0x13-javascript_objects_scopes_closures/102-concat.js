#!/usr/bin/node
// import file system module
const fs = require('fs');

// read the content of the first file into the third file
// syntax of readFile is file path, optional format annd call function
fs.readFile(process.argv[2], (err, inputD) => {
  if (err) throw err;

  // write the read content into the third file
  fs.writeFile(process.argv[4], inputD, (err) => {
    if (err) throw err;
  });
});

// repeat process, but append this time
// signify append flag when writing the file, so the previous
// content is not erased
fs.readFile(process.argv[3], (err, inputD) => {
  if (err) throw err;
  fs.writeFile(process.argv[4], inputD, { flag: 'a' }, (err) => {
    if (err) throw err;
  });
});
