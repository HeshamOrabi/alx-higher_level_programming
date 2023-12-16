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

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
    this.print();
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
    this.print();
  }
}

module.exports = Rectangle;
