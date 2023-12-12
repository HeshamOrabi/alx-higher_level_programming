#!/usr/bin/node

const args = process.argv.slice(2);
let len = 0;

args.forEach(() => {
  len++;
});

if (len === 0) {
  console.log('No argument');
} else if (args[0]) {
  console.log(args[0]);
}
