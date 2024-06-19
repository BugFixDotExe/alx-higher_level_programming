#!/usr/bin/node
let digits = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    digits.push(parseInt(process.argv[i]));
  }
  digits = digits.sort((a, b) => a - b);
  console.log(digits[digits.length - 2]);
}
