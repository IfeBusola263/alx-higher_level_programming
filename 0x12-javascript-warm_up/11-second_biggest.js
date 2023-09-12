#!/usr/bin/node

const len = process.argv.length;
if (len < 3 || len === 3) {
  console.log(0);
} else {
  const sorted = [...process.argv].sort((a, b) => a - b);
  console.log(sorted[len - 2]);
}
