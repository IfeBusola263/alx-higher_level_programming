#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
let i = 0;
const newlist = list.map((num) => num * i++);
console.log(newlist);
