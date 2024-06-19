#!/usr/bin/node
const userInput = parseInt(process.argv[2]);
if (isNaN(userInput)) {
  console.log('Missing number of occurrences');
} else if (userInput <= 0) {
  console.log();
} else {
  for (let i = 0; i < userInput; i++) {
    console.log('C is fun');
  }
}
