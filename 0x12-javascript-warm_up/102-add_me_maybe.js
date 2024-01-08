#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  x++;
  theFunction(x);
};
