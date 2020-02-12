#!/usr/bin/node
'use strict';
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], { json: true }, function (e, r, b) {
  if (e) console.log(e); else {
    if (r.statusCode === 200) console.log(b.title);
  }
});
