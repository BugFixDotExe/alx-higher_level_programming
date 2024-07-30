#!/usr/bin/node
const request = require('request');
try {
  request(process.argv[2], (err, res, body) => {
    if (err) {
      console.log('Code: ', err);
    }
    console.log('Code: ', res.statusCode);
  });
} catch (e) {
}
