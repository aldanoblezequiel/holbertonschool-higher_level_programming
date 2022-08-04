#!/usr/bin/node
const argument = process.argv;
if (argument.length < 2 || isNaN(parseInt(argument[2]))) {
  console.log(factorial(1));
} else {
  console.log(factorial(parseInt(argument[2])));
}
function factorial (n) {
  if (n < 0) { return; }
  if (n === 1) { return 1; }
  return n * factorial(n - 1);
}
