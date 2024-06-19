#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else if (size <= 0) {
  console.log();
} else {
  for (let j = 0; j < size; j++) {
    console.log('X'.repeat(size));
  }
}
