#!/usr/bin/node

const len = process.argv.length;
if (len < 3) {
  console.log(1);
} else {
  let num = 1;
  for (let i = Number(process.argv[2]); i !== 0; i--) {
    num *= i;
  }
  console.log(num);
}
