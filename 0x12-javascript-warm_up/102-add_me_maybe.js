#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  num = number + 1;
  theFunction(String(num));
}

exports.addMeMaybe = addMeMaybe;
