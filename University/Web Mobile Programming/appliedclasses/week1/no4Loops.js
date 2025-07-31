for (let i = 1; i <= 3; i++) {
    console.log("Try #" + i)
}

/*
Expression 1 is executed (one time) before the execution of the code block.
Expression 2 defines the condition for executing the code block.
Expression 3 is executed (every time) after the code block has been executed.
*/

for (let n = 2; n <= 10; n = n+1 ) {
    if (n % 2 === 0) {
        console.log(n)
    }
}