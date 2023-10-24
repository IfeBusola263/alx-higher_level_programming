#!/usr/bin/node
// import the required module - request
const request = require('request');
const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body);

    const characters = film.characters;

    characters.forEach((character) => {
      request(character, (err, response, info) => {
        if (err) {
          console.log(err);
        }
        const characterInfo = JSON.parse(info);
        console.log(characterInfo.name);
      });
    });
  }
});
