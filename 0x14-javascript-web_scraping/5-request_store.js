#!/usr/bin/node
const request = require('request');
const fs = require('fs');

try {
  if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
    request(process.argv[2], (err, res, body) => {
      if (err) {
        console.log('Code: ', err);
      }
      fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
        if (err) {
          console.log('Error: ', err);
        }
      });
    });
  }
} catch (e) {
}
