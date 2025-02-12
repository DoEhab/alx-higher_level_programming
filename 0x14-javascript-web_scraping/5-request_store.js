#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request.get(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    fs.writeFile(filePath, data);
  }
});
