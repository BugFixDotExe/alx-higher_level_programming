#!/usr/bin/node
function add (a, b) {
  let sumOfInt;
  if (a === undefined && b === undefined) {
    console.log('NaN');
  } else if (a === undefined || b === undefined) {
    console.log('NaN');
  } else {
    sumOfInt = parseInt(process.argv[2]) + parseInt(process.argv[3]);
    console.log(sumOfInt);
  }
}
add(process.argv[2], process.argv[3]);
