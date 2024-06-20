#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  if (list === undefined) { return; } else {
    for (let i = list.length; i >= 0; i--) {
      if (list[i] === undefined) {
        continue;
      }
      reversedList.push(list[i]);
    }
  }
  return (reversedList);
};
