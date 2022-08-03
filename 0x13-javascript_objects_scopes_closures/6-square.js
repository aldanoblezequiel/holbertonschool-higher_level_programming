#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) super.print();
    else {
      for (let n = 0; n < this.size; n++) {
        for (let i = 0; i < this.size; i++) process.stdout.write(c);
        console.log('');
      }
    }
  }
};
// require use
