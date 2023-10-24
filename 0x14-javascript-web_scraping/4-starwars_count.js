#!/usr/bin/node
// import the required module
const request = require('request');

// The api comes in as an argument
const api = process.argv[2];

// this is the people ID of the character Wedge Antilles
// You need to look at the JSON from https://swapi-api.alx-tools.com/api/films/
// to understand the structure of the data
const charNum = '18';

// This is a counter to get the number of films Wedge Antilles appears in
let num = 0;

// The get resquest is made
// if any error, that would be the first response
// if not, a response and body object is returned
request(api, (error, response, body) => {
  // Display the error if any arises
  if (error) {
    console.log(error);
  }
  // JSON.parse deserializes the JSON object in the body variable
  const data = JSON.parse(body);

  // collecting the result member of the Object
  const results = data.results;

  // loop through the list of dictioanries with each film data
  // Look to extract the characters member of the result, which is an array
  // The array has a list of urls to each character in each episode
  for (let i = 0; i < results.length; i++) {
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j].includes(charNum)) {
        num = num + 1; // count the number to times the number 18 is found in the urls
      }
    }
  }
  console.log(num); // This would be the number of times this person has appeared in all episodes
});
