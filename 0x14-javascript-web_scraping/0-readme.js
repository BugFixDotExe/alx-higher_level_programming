#!/usr/bin/node

const fs = require('fs');
try {
  fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
} catch (e) {
}
