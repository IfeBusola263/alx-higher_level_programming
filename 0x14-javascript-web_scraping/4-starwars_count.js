#!/usr/bin/node
// import the required module
const request = require('request');

const api = process.argv[2];
const charNum = '18';
let num = 0;

request(api, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const results = data.results;

  for (let i = 0; i < results.length; i++) {
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j].includes(charNum)) {
        num = num + 1;
      }
    }
  }
  console.log(num);
});
