#!/usr/bin/node
let funcCalls = 0;
exports.logMe = function (item) {
  console.log(funcCalls + ': ' + item);
  funcCalls++;
};
