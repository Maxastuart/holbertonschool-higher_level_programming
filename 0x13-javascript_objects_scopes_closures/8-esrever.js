#!/usr/bin/node
'use strict';
exports.esrever = function (list) {
  const list2 = [];
  let n = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    list2[n] = list[i];
    n++;
  }
  return list2;
};
