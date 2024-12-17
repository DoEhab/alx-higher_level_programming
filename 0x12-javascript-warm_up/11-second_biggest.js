#!/usr/bin/env node

const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
    console.log(0);
    return;
}
args.sort();
console.log(args[args.length - 2]);
