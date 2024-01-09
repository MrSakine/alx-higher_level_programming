#!/usr/bin/node
const fs = require('node:fs');
const args = process.argv.splice(2);
const fileA = fs.readFileSync(args[0], 'utf8');
const fileB = fs.readFileSync(args[1], 'utf8');
let content = fileA;
content += fileB;
fs.writeFileSync(args[2], content, 'utf-8');
