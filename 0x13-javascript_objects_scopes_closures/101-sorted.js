#!/usr/bin/node
const dict = require('./101-data.js').dict;
const sorted = Object.keys(dict).map(function (key) {
  return [key, dict[key]];
});
sorted.sort(function (first, second) {
  return first[1] - second[1];
});
const newdict = {};
let flag = sorted[0][1];
let array = [];
for (let item = 0; item < sorted.length; item++) {
  if (sorted[item][1] === flag) {
    array.push(sorted[item][0]);
  } else {
    newdict[flag] = array;
    flag = sorted[item][1];
    array = [];
    item--;
  }
  newdict[flag] = array;
}
console.log(newdict);
// vpi yen
