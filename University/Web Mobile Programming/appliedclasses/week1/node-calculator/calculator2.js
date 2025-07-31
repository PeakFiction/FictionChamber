// Extract the command line arguments (skipping the first two default ones)
const args = process.argv.slice(2);

// Check that the user provided exactly 3 arguments
if (args.length !== 3) {
    console.log('Usage: node calculator.js [number1] [operator] [number2]');
    process.exit(1); // Exit with an error code
}

// Convert the first and third arguments to numbers
const num1 = parseFloat(args[0]);       // First number
const operator = args[1];               // Operator (+, -, *, /)
const num2 = parseFloat(args[2]);       // Second number

let result; // Variable to store the calculation result

// Perform the correct operation based on the operator provided
switch (operator) {
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '/':
        // Check for division by zero
        if (num2 === 0) {
            console.log('Error: Division by zero');
            process.exit(1);
        }
        result = num1 / num2;
        break;
    default:
        // If the operator is not recognized, display an error
        console.log('Error: Invalid operator');
        process.exit(1);
}

// Print the result to the terminal in a readable format
console.log(`${num1} ${operator} ${num2} = ${result}`);