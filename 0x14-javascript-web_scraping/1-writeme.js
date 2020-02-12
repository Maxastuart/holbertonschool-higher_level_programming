#!/usr/bin/node
'use strict';
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err, data) => {
  if (err) console.log(err);
});
