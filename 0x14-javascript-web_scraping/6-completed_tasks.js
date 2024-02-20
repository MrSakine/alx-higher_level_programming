#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request('https://jsonplaceholder.typicode.com/users/', function (error, response, body) {
  if (error) console.log(error);
  const users = JSON.parse(body);
  request(url, function (error, response, body) {
    if (error) console.log(error);
    const data = JSON.parse(body);
    const result = {};

    for (const user of users) {
      const completed = data.filter(value => value.userId === user.id && value.completed === true).length;
      result[user.id] = completed;
    }

    console.log(result);
  });
});
