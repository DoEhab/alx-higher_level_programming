#!/usr/bin/node
const fileStream = require('fs');
const fileName = process.argv[2];
const text = process.argv[3];
fileStream.writeFile(fileName, text, err => {
  if (err) {
    console.log(err);
  }
});
