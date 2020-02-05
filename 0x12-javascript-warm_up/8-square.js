#!/usr/bin/node
'use strict';
let i = 0;
while (i < process.argv[2]) {
  let n = 0; let x = '';
  while (n < process.argv[2]) {
    x += 'X';
    n++;
  }
  console.log(x);
  i++;
}
