#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  if (list === undefined) {
    return (occurence);
  }
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurence += 1;
    }
  }
  return (occurence);
};
