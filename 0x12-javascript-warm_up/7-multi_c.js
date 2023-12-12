#!/usr/bin/node

const args = process.argv.slice(2);
let num = parseInt(args[0], 10);

if (args.length === 0) {
  console.log('Missing number of occurrences');
}

if (!isNaN(num)) {
  for (; num > 0; num--) {
    console.log('C is fun');
  }
}
