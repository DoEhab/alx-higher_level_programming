#!/usr/bin/node
const fileStream = require('fs');
if (process.argv[2]) {
  const fileName = process.argv[2];
  const text = process.argv[3];
  fileStream.writeFile(fileName, text, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
}
