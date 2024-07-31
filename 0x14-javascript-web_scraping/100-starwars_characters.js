#!/usr/bin/node
const request = require('request');
try {
  if (process.argv[2] !== undefined) {
    request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, con, body) => {
      if (err) {
        console.log(err);
        return;
      }
      if (con.statusCode !== 200) {
	      return;
      }
      const fullContent = JSON.parse(body);
      for (let i = 0; i < fullContent.characters.length; i++) {
        request(fullContent.characters[i], (err, con, body) => {
          if (err) {
            console.log(err);
            return;
          }
          console.log(JSON.parse(body).name);
        });
      }
    });
  }
} catch (e) {
}
