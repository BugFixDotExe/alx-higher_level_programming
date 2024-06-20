#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined || c !== 'C') {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
