#!/usr/bin/env node

if (process.argv[2]) {
  console.log(process.argv[2]);
} else if (!process.argv[2]) {
  console.log('No argument');
}
