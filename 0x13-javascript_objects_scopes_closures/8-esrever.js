#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const rev = [];
  for (let i = len; i > 0; i--) {
    rev.push(list[i - 1]);
  }
  return rev;
};
