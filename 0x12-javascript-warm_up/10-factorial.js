#!/usr/bin/node

const args = process.argv.slice(2);

const num = parseInt(args[0]);

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(num));
