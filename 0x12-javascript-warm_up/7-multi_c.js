#!/usr/bin/node
const arg = process.argv[2];
const notANumber = 'Missing number of occurrences';
const parsedNumber = Number.parseInt(arg);
if (arg === undefined || isNaN(parsedNumber)) {
  console.log(notANumber);
} else {
  for (let i = 0; i < parsedNumber; i++) {
    console.log('C is fun');
  }
}
