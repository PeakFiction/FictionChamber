function imperative(nums) {
  const result = [];
  // collect squares of evens
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    if (n % 2 === 0) {
      result[result.length] = n * n;
    }
  }
  // simple (but slow) insertion-sort, descending
  for (let i = 1; i < result.length; i++) {
    let key = result[i], j = i - 1;
    while (j >= 0 && result[j] < key) {
      result[j + 1] = result[j];
      j--;
    }
    result[j + 1] = key;
  }
  return result;
}

function functional(nums) {
  return [...nums]                     // shallow copy
    .filter(n => n % 2 === 0)          // keep evens
    .map(n => n * n)                   // square each
    .sort((a, b) => b - a);            // descending
}

numsExample = [1,2,3,4,5]
console.log(imperative(numsExample))
console.log(functional(numsExample))
