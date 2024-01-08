#!/usr/bin/node
function arrayMax (arr) {
  let len = arr.length;
  let max = arr[0];
  while (len--) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
}

function secondBiggest (array, m, n) {
  if (array.length === 0) {
    return (0);
  } else if (m !== n) {
    return (n);
  } else {
    m = arrayMax(array);
    if (m) {
      array.splice(array.indexOf(m), 1);
      n = arrayMax(array);
    }
  }
  return secondBiggest(array, m, n);
}

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(secondBiggest(args.slice(2), null, null));
}
