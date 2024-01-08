#!/usr/bin/node
const arg = process.argv[2];
const notANumber = 'Not a number';
const parsedNumber = Number.parseInt(arg);
console.log(arg === undefined || isNaN(parsedNumber) ? notANumber : 'My number:' + (' ' + parsedNumber));
