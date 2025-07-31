const args = process.argv.slice(2);

if (args.length != 3) {
    console.log('Usage: node calculator.js [number1] [operator] [number2]');
    process.exit(1)
}

console.log(args)
var firstNumber = parseFloat(args[0]);
var operator = args [1];
var secondNumber = parseFloat(args [2]);

console.log(operator)
let result;

switch (operator) {
    case '+':
        result = firstNumber + secondNumber;
        console.log(result)
        break;
    case '-':
        result = firstNumber - secondNumber;
        console.log(result)
        break;
    case 'x':
            result = firstNumber * secondNumber;
            console.log(result)
            break;
    case '/':
            if (secondNumber === 0) 
            {
                console.log("Can't Divide by 0")
                break;
            } else {
                result = firstNumber / secondNumber;
                console.log(result)
                break;
            }

    default:
        console.log("Invalid Operator")
        process.exit(1)
}

