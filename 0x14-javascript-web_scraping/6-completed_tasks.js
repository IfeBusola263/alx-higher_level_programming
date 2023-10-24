#!/usr/bin/node
// import the required module - request
const request = require('request');

// Make request and format output to display
// employee ID and number of completed task
request(process.argv[2], (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    const toDo = JSON.parse(data);

    const dict = {};

    for (let i = 1; i < 11; i++) {
      let completed = 0;

      for (let j = 0; j < toDo.length; j++) {
        if (i === toDo[j].userId && toDo[j].completed === true) {
          completed = completed + 1;
        }
        // console.log(to_do[j].completed);
      }
      dict[i.toString()] = completed;
    }
    console.log(dict);
  }
});
