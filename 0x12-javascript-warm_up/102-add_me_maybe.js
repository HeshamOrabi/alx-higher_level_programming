#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  theFunction(String(number + 1));
}

exports.addMeMaybe = addMeMaybe;
