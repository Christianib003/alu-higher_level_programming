#!/usr/bin/node
let items = 0;

exports.logMe = function (item) {
  console.log(`${items}: ${item}`);
  items++;
};
