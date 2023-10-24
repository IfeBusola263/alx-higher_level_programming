#!/usr/bin/node
// import the required module
const request = require('request');

const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// response object
request(api, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
