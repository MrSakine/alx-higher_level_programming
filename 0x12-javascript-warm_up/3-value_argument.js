#!/usr/bin/node
const arg = process.argv[2];
const notFound = 'No argument';
console.log(!arg ? notFound : arg);
