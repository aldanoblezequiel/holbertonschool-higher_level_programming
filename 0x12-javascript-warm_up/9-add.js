#!/usr/bin/node
const argument = process.argv;
const first = parseInt(argument[2]);
const second = parseInt(argument[3]);
function add (first, second) {
  console.log(first + second);
}
add(first, second);
