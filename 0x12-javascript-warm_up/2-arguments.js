#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.length - 2;
const notFound = 'No argument';
const found = 'Argument found';
const many = 'Arguments found';
console.log(args <= 0 ? notFound : args === 1 ? found : many);
