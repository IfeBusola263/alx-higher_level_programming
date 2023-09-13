#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const rev = [];
  for (let i = len - 1; i < 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
