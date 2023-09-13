#!/usr/bin/node

const Squ = require('./5-square.js');

module.exports = class Square extends Squ {
  // Check if c is defined
  charPrint (c) {
    if (c === undefined) {
      // if c is not defined the character is changed
      c = 'X';
    }

    // loop to print the square by binding the size to this module
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};
