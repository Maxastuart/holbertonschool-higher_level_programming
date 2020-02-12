#!/usr/bin/node
'use strict';
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (e, r, b) {
  if (e) console.log(e); else if (r.statusCode === 200) {
    fs.writeFile(process.argv[3], b, (err, data) => {
      if (err) console.log(err);
    });
  }
});
