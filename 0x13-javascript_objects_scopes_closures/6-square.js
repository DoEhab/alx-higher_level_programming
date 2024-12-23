#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print(this.height);
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
