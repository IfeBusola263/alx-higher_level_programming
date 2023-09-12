#!/usr/bin/node

const len = process.argv.length;
if (len < 3) {
  console.log(1);
}

function factorial (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(Number(process.argv[2])));
