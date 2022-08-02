#!/usr/bin/node
const argument = process.argv;
const idx = parseInt(argument[2]);
if (isNaN(idx)) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < idx; index++) {
  console.log('C is fun');
}
