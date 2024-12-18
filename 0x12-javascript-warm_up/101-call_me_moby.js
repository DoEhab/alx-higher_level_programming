#!/usr/bin/node

module.exports = function callMeMoby(count, callback) {
  for (let i = 0; i < count; i++) {
    callback();
  }
}
