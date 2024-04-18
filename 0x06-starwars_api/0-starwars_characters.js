#!/usr/bin/node

const req = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

req(url, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character in characters) {
      const res = await new Promise((resolve, reject) => {
        req(characters[character], (err, res, html) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});
