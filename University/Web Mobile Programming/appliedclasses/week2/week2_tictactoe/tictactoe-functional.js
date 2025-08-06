 // Import Node.js dependencies

var prompt = require("prompt-sync")({
    sigint: true
});
/**
 * Resets the game for when the app runs & repeats
 */
function main() {

        // Global variables

    let empty = " ";
    const boardLength = 3;
    const playerOne = "X";
    const playerTwo = "O";
    let playerOnesTurn;
    let board;
    let winner;

    // Messages

    const invalidInput = "Wrong input. Please try again.";
    const outOfBounds = "Position out of bounds. Please try again.";
    const positionFilled = "Position already filled. Please try again.";
    const drawMessage = "The game ended in a draw.";
    const replayPrompt = "Do you wish to play again?";
    const movePrompt = function(sym) {
        return `Player ${sym}, please enter the index of your next move: `;
    };
    const winMessage = function(player) {
        return `\nPlayer ${player} has won the game.`;
    }

    // Winning trios

    const winningTrios = new Array(
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    );

    /**
     * This function will print out the board game into the console.
     * @param {array} board - An array containing the values for each position on the board.
     * @param {number} padding - How many spaces should appear either side of the values.
     */

    function printGameBoard(board, padding = 1) {
    let horizontalDivider = "-".repeat((boardLength * (2 * padding + 1) + 2));
    for (let rowIndex = 0; rowIndex < boardLength; rowIndex++) {
        if (rowIndex != 0) {
            console.log(horizontalDivider);
        }
        let start = rowIndex * boardLength;
        let row = board.slice(start, start + boardLength);
        let rowNew = [];
        for(let i = 0; i < row.length; i++) {
            rowNew.push(empty.repeat(padding) + `${row[i]}` + empty.repeat(padding));
        }
        row = rowNew;
        console.log(row.join("|"));
    }
    console.log(" ");
    }

    /**
     * Resets the game to a valid starting state.
     */
    function resetGame() {
        playerOnesTurn = true;
        board = Array.from(Array(boardLength ** 2), function() {
            return " ";
        });
        winner = null;
    }


    function game() {
        /**
         * Identify which player is currently playing.
         * @returns Get the string corresponding to the player whose turn it is.
         */
        function getCurrentPlayer() {
            if (playerOnesTurn) {
                return playerOne;
            }
            return playerTwo;
        }


        /**
         * To check if there is any winner from the current state of the gameboard.
         * @returns true if there is a winner.
         */
        function checkWin(board, player, winningTrios) {
            const positions = board
                .map((cell, index) => cell === player ? index : null)
                .filter(index => index !== null);

            return winningTrios.some(trio =>
                trio.every(index => positions.includes(index))
            );
        }

        /**
         * Plays a Tic Tac Toe game through to completion.
         */
        function play() {
            while (!isOver(board, empty, winner)) {
                printGameBoard(board);
                
                // Prompt the next player for a move
                let index = getNextMove();

                // Perform out of bounds checks
                if (!(0 <= index < boardLength ** 2)) {
                    console.log(outOfBounds);
                    continue;
                }
                
                // Check if position already filled
                if (board[index] != empty) {
                    console.log(positionFilled);
                    continue;
                }
                // Enact the move on the board
                board[index] = getCurrentPlayer();

                // Check for end game conditions
                const currentPlayer = getCurrentPlayer();
                if (checkWin(board, currentPlayer, winningTrios)) {
                    winner = currentPlayer;
                    return;
                }


                // Flip the turn
                playerOnesTurn = !playerOnesTurn;
            }
        }

        /**
         * Repeatedly prompts the user for their next move until they give a
         * numerical index, which it returns.
         * Doesn't perform out of bounds validity checks on the supplied index.
         * @returns user input move.
         */
        function getNextMove() {
            let move, userIn;
            while (true) {
                userIn = prompt(movePrompt(getCurrentPlayer()));
                move = Number(userIn);

                // Check validity and return the move if true
                if (isNaN(move) || move < 0 || move > 8) {
                    console.log(invalidInput);
                    continue;
                }
                return move;
            }
        }


        /**
         * To check if all the grid has been filled and no winner is presence.
         * @returns true if no winner and all the available index is filled by users.
         */
        function hasDrawn(board, empty) {
            return board.every(cell => cell !== empty);
        }


        /**
         * Check if the game is over
         * @returns Returns true if the game is over.
         */
        function isOver(board, empty, winner) {
            return hasDrawn(board, empty) || winner !== null;
        }

        /**
         * Prints winning or drawing info after the game has completed.
         */
        function displayWinnerInfo() {
            if (winner === null) {
                console.log(drawMessage);
            } else {
                console.log(winMessage(winner));
            }
        }

        play();
        displayWinnerInfo();
    }

    while (true) {
        resetGame();
        game();
        // Ask user if they want to play again
        if (prompt(replayPrompt) != "y") {
            break;
        }
        resetGame();
    }
}

main();