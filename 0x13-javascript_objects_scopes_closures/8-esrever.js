#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];

  for (let i = 0; i < list.length; i++) {
    listRev.unshift(list[i]);
  }
  return listRev;
};
