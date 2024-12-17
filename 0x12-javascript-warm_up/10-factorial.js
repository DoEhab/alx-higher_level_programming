#!/usr/bin/env node

const i = Number(process.argv[2]);

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 0 || a === 1) {
    return 1;
  }
  return factorial(a - 1) * a;
}

console.log(factorial(i));
