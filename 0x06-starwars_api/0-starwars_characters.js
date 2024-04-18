#!/usr/bin/node

const req = require('request');
const movie = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movie}`;

req(url, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      req(characterId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
