#!/usr/bin/node
const dict = require('./101-data.js').dict;
const mySet = new Set();
const newDict = {};
// create a distinct set of the values
for (const value of Object.values(dict)) {
  mySet.add(value);
}

/*
  create a new dictionary
  with the unique values as keys
*/
for (const item of mySet) {
  const newArr = [];
  for (const [key, value] of Object.entries(dict)) {
    if (item === value) {
      newArr.push(key);
      newDict[item] = newArr;
    }
  }
}

console.log(newDict);
