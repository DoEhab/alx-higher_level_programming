#!/usr/bin/node

const request = new Request(process.argv[2], {
  method: 'GET'
});

fetch(request).then((response) => {
  console.log({ code: response.status.code });
});
