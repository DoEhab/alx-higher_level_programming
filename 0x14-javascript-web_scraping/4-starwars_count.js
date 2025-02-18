#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (!error) {
    let counter = 0;
    const data = JSON.parse(body);
    data.results.forEach(element => {
      element.characters.forEach((characterUrl) => {
        // Check if the character URL ends with "/18/"
        if (characterUrl.includes('/18/')) {
          counter++;
        }
      });
    });
    console.log(counter);
  }
});
