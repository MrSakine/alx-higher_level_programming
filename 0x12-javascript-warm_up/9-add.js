#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const args = process.argv;
const firstNumber = Number.parseInt(args[2]);
const secondNumber = Number.parseInt(args[3]);
console.log(add(firstNumber, secondNumber));
