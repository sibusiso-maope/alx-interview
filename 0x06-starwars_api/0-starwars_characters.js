#!/usr/bin/node

const request = require('request');

const req = (arr, k) => {
  if (k === arr.length) return;
  request(arr[k], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      req(arr, k + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      req(chars, 0);
    }
  }
);
