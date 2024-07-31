#!/usr/bin/node
const request = require('request');
try {
  request(process.argv[2], (err, res, body) => {
    if (err) {
      console.log('code:', err);
    }
    console.log('code:', res.statusCode);
  });
} catch (e) {
}
