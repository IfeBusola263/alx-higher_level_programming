#!/usr/bin/node

const len = process.argv.length;
const num = Number(process.argv[2]);
if (len < 3 || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(num)}`);
}
