#!/usr/bin/node

const len = process.argv.length;
const num = Number(process.argv[2]);
const text = 'C is fun';
if (len < 3) {
  console.log('Missing number of occurrences');
} else {
  if (!(isNaN(num)) && num > 0) {
    for (let i = 0; i < num; i++) {
      console.log(text);
    }
  }
}
