#!/usr/bin/node
const list = require('./100-data').list;
const mylist = list.map((value, index) => {
  return (value * index);
});
console.log(list);
console.log(mylist);
