#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], (err, inputD) => {
  if (err) throw err;
  fs.writeFile(process.argv[4], inputD, (err) => {
    if (err) throw err;
  });
});

fs.readFile(process.argv[3], (err, inputD) => {
  if (err) throw err;
  fs.writeFile(process.argv[4], inputD, { flag: 'a' }, (err) => {
    if (err) throw err;
  });
});
