#!/usr/bin/node

exports.esrever = function (list) {
  let element;
  const newList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    element = list.pop();
    newList.push(element);
  }

  return (newList);
};
