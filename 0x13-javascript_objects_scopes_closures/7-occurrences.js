#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, item) => {
    if (item === searchElement) {
      count++;
    }
    return count;
  }, 0);
};
