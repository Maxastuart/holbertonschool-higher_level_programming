#!/usr/bin/node
'use strict';
const fs = require('fs');
const request = require('request');

request(process.argv[2], { json: true }, function (e, r, b) {
  if (e) console.log(e); else if (r.statusCode === 200) {
    const count = {};
    b.forEach(t => {
      if (count[t.userId] === undefined) count[t.userId] = 0;
      if (t.completed === true) count[t.userId]++;
    });
    console.log(count);
  }
});
