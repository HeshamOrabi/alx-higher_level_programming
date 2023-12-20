#!/usr/bin/node

const ar = require('./100-data.js').list;

const arr = ar.map((x, idx) => x * idx);

console.log(ar);
console.log(arr);
