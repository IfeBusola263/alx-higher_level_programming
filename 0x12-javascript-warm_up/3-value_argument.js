#!/usr/bin/node

const len = process.argv.length;
if (len < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
