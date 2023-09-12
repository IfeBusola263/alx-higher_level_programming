#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Declare counter
  let count = 0;

  // Use the foreach method to iterate through the array
  list.forEach((element) => {
    if (element === searchElement) {
      // increament when match is found
      count = count + 1;
    }
  });
  return count;
};
