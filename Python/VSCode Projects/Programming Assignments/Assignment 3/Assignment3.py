import random
from tkinter import *

class MazeRunner:
    def __init__(self):
        window = Tk() #TODO: Create a window
        window.title('Escape the Maze')  #TODO: Set a title

        # TODO: Create and add a frame to window
        frame1 = Frame(window)
        frame1.pack()
        
        # TODO: Create matrix representation
        self.maze = ...
        self.sol = ...
        self.size = StringVar()
        
        # TODO: Create necessary label, entry, or buttons. Don’t forget
        # to position them accordingly using the grid system
        
        ...
        ...
        self.canvas = Canvas(window, bg="white")
        self.canvas.pack()
        window.mainloop()
        
        # TODO: Create the visualization of the maze from the matrix representation
    
    def createMaze(self):
        ...  # TODO: Clear the canvas
        height = self.canvas.winfo_reqheight()
        width = self.canvas.winfo_reqwidth()
        mazeSize = ...
        self.maze = [[random.randint(..., ...) for j in range(...)]
                    for i in range(...)]
        self.maze[0][0] = 1
        
        # TODO: Complete the isSafe function
    def isSafe(..., ..., ..., ..., ...):
        if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == ...:
            return ...
        return ...
    def solveMazeRecur(maze, x, y, sol, N):
        # If (x, y is goal) return True
        if x == N - 1 and y == N - 1:
            ...
            ...
            
        if ...(maze, x, y, N) == ...:
            # Check if maze[x][y] is valid
            self.sol[x][y] = ...
            # Move forward in x direction
            if self.solveMazeRecur(..., ..., ..., ..., ...) == ...:
                return ...
        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if self.solveMazeRecur(..., ..., ..., ..., ...) == ...:
            return ...  
        
        # If the path is invalid
            # BACKTRACK: unmark x, y as part of solution path
            self.sol[x][y] = ...
            return ...
        
        def solveMaze(...):
        # TODO: Create the visualization of the escape route
        mazeSize = ...
        height = self.canvas.winfo_reqheight()
        width = self.canvas.winfo_reqwidth()
        
        # TODO: Use list comprehension to create the matrix representation containing all 0 for the solution
        self.sol = [[...] for i in range(mazeSize)]
        
        # TODO: Call the recursive function
        if self.solveMazeRecur(self.maze, ..., ..., self.sol, ...) == ...:
            self.canvas.create_text(...)
        
        # TODO: Initialize positions of x’s and y’s
... ... ...
        # TODO: Create the visualization of the solved maze
... ... ...
        return ...
MazeRunner()  # TODO: Create GUI

