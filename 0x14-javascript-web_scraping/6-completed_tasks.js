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

    toDo.forEach((task) => {
      if (task.completed) {
        dict[task.userId] = (dict[task.userId] || 0) + 1;
      }
    });
    console.log(dict);
  }
});
