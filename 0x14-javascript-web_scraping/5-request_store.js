#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request.get(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(filePath, body, (err) => {
      if (err) {
        console.error('File write error:', err);
      }
    });
  }
});
