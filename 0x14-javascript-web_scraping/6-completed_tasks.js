#!/usr/bin/node
const request = require('request');
try {
  const userTask = {};
  if (process.argv[2] !== undefined) {
    request(process.argv[2], (err, res, body) => {
      if (err) {
        console.log(err);
      }
      const userObj = JSON.parse(body);
      for (let item = 0; item < userObj.length; item++) {
        if (userObj[item].completed === true) {
          userTask[userObj[item].userId] = 0;
        }
      }
      for (let item = 0; item < userObj.length; item++) {
        if (userObj[item].completed === true) {
          userTask[userObj[item].userId] += 1;
        }
      }
      console.log(userTask);
    });
  }
} catch (e) {
}
