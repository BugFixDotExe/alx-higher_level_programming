#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      var obj = {}
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
