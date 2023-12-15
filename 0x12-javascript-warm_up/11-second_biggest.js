#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const newArgs = [];

if (args.length < 2) {
  console.log(0);
} else {
  const newArgs = args.sort((a,b) => b - a);

  if (newArgs.length === 2) {
    console.log(newArgs[0]);
  } else {
    console.log(newArgs[1])
  }
}
