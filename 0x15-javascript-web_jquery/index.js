#!usr/bin/node
const fs = require('node:fs');

const numbers = [...Array(10).keys(), 100, 101, 102, 103];
let list = '<ul>';
for (const number of numbers) {
  list += `<li><a href="${number}-main.html" target="_blank">Task ${number}</a></li>`;
}
list += '</ul>';
fs.writeFileSync('index.html', `
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header>All tasks</header>
    ${list}
  </body>
</html>
`);
