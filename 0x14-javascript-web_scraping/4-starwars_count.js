#!/usr/bin/node
const request = require('request');
try {
  if (process.argv[2] !== undefined) {
    const endPoint = `${process.argv[2]}`;
    request(endPoint, (err, res, body) => {
      if (err) {
        console.log('Code: ', err);
      }
      if (res.statusCode === 200) {
        const jsonToObj = JSON.parse(body);
        request(jsonToObj.results[0].characters[15], (err, res, body) => {
          if (err) {
            console.log('Code: ', err);
          }
          if (res.statusCode === 200) {
            const userObj = JSON.parse(body);
            console.log(userObj.films.length);
          }
        });
      }
    });
  }
} catch (e) {
}
