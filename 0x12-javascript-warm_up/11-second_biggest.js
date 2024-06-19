#!/usr/bin/node
const digits = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    digits.push(process.argv[i]);
  }
  digits.sort();
  console.log(digits[digits.length - 2]);
}
