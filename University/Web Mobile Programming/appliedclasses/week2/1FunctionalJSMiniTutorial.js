/* Map Function - Transforms Data */

const numbers1 = [1, 2, 3];

const doubled1 = numbers1.map (n => n * 2);

console.log(doubled1)
console.log("==============================")
console.log()

let prices1 = [3.5, 7, 1.25];

let cents1 = prices1.map(p => p * 10);

console.log(cents1)
console.log("==============================")
console.log()

/* Filter Function - removes unwanted items */
let scores1 = [82, 42, 90]
let passed1 = scores1.filter(score => score >= 50);
console.log(passed1)
console.log("==============================")
console.log()

let nums1 = [1,2,3,4,5,6];
let evens1 = nums1.filter(n => n % 2 === 0);
console.log(evens1)
console.log("==============================")
console.log()

/* Reduce() - combines values into one */
let total1 = [5, 10, 20].reduce((acc, val) => acc + val, 0);
/* Like a for loop, 
Acc = Accumulator
val = Current value 

acc + val is the operation
0 is the starting value
*/ 
console.log(total1)
console.log("==============================")
console.log()


let names1 =  ["Ada", "Grace", "Linus"];
let totalChars = names1.reduce((acc, names1) => acc+ names1.length, 0)
console.log(totalChars)
console.log("==============================")
console.log()

/* Fill in the Blank Challenge, Sum the Squares of Odd Numbers Only */
let numbers = [1,2,3,4,5];
let result = numbers
    .filter(n => n % 2 !== 0) /* Filter to be Odd Numbers Only */
    .map(n => n * n) /* Map it, Make Every Element in the Numbers Array multiply by itself */
    .reduce((sum, val) => sum + val, 0);

console.log(result);
console.log("==============================")
console.log()