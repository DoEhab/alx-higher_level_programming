#!/usr/bin/node

const argsLength = process.argv.slice(2).length;
argsLength === 0 ? console.log('No argument') : argsLength === 1 ? console.log('Argument found') : console.log('Arguments found');
