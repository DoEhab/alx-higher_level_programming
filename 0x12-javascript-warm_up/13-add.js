#!/usr/bin/node

const i = Number(process.argv[2]);
const j = Number(process.argv[3]);

add = function (a, b) {
  console.log(a + b);
}

add(i, j);
