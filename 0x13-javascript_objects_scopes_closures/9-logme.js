#!/usr/bin/node

const ar = [];
exports.logMe = function (item) {
  ar.push(item);
  console.log(`${ar.length - 1}: ${item}`);
};
