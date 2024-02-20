#!/usr/bin/node
const request = require('request');

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);
  printCharacters(data.characters, 0);
});
