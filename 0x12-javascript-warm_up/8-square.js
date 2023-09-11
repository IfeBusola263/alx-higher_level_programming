#!/usr/bin/node

const len = process.argv.length;
const num = Number(process.argv[2]);
const text = 'X';
if (len < 3 || isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write(text);
    }
    console.log();
  }
}
