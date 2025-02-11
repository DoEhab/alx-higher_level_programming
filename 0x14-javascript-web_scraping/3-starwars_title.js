#!/usr/bin/node
const { url } = require('inspector');
const request = require('request');
movie_id = process.argv[2];
url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;
request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
