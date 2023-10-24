#!/usr/bin/node
// import the required module which is request
const request = require('request');

request(process.argv[2], (err, response, body) => {
    if (err) {
	console.log(err);
    } else {
	console.log("code: ${response.statusCode}");
    }
});
