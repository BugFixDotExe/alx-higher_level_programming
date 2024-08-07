#!/usr/bin/node
const request = require('request');
try {
  if (process.argv[2] !== undefined) {
    const endPoint = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
    request(endPoint, (err, res, body) => {
      if (err) {
        console.log('Code: ', err);
      }
      if (res.statusCode === 200) {
        const jsonToObj = JSON.parse(body);
        console.log(jsonToObj.title);
      }
    });
  }
} catch (e) {
}
