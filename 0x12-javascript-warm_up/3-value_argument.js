#!/usr/bin/node
let index = 2;
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  while (process.argv[index] !== undefined) {
    console.log(process.argv[index]);
    index++;
  }
}
