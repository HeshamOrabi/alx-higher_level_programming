#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (; x > 0; x--) {
    theFunction();
  }
}

exports.callMeMoby = callMeMoby;
