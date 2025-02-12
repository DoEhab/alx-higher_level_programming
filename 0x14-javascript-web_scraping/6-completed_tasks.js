#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const result = {};
    data.forEach(element => {
      if (element.completed) {
        result[element.id] = element.userId;
      }
    });
    console.log(result);
  }
});
