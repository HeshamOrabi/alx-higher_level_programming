#!/usr/bin/node

const args = process.argv.slice(2);
const newArgs = [];

if (args.length < 2) {
  console.log(0);
} else {
  for (let len = args.length - 1; len >= 0; len--) {
    newArgs.push(parseInt(args[len]));
  }

  newArgs.sort();

  console.log(newArgs[newArgs[newArgs.length - 2]]);
}
