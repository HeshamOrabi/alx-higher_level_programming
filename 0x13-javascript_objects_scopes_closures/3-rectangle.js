#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = this.height; h > 0; h--) {
      let s = '';
      for (let w = this.width; w > 0; w--) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
