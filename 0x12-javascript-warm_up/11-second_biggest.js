#!/usr/bin/node

const args = process.argv.slice(2);
let new_args = []

if (args.length < 2) {
  console.log(0)
} else {
  for (let len = args.length - 1; len >= 0; len--) {
    new_args.push(parseInt(args[len]));
  }
  
  new_args.sort();
  
  console.log(new_args[new_args[new_args.length - 2]]);
}
