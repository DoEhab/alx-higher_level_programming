#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  let i = process.argv[2];
  let j = i;
  while (i > 0) {
    console.log('X'.repeat(j));
    i--;
  }
} else {
  console.log('Missing size');
}
