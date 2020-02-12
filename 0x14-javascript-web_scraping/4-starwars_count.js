#!/usr/bin/node
'use strict';
const request = require('request');

request(process.argv[2], { json: true }, function (e, r, b) {
  if (e) console.log(e); else {
    if (r.statusCode === 200) {
      let count = 0;
      b.results.forEach(film => {
        film.characters.forEach(char => {
          if (char.search('18') >= 0) count++;
        });
      });
      console.log(count);
    }
  }
});
