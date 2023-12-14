#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Missing size')
} else {
  for (let i = args[0]; i > 0; i--) {
    let line = ''
    for (let j = args[0]; j > 0; j--) {
      line += 'X';
    }
    console.log(line);
  }
}
