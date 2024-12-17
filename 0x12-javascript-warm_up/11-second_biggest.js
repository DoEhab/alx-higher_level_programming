#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
  process.exit(0);
}
args.sort();
console.log(args[args.length - 2]);
