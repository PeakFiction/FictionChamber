#Muhammad Sakhran Thayyib, PA3, 2206046790
import random
from tkinter import *

class MazeRunner:
    def __init__(self):
        mainWindow = Tk() #Creates the tkinter window
        mainWindow.title('Escape the Maze') #Sets the main window name as 'Escape the Maze

        MainFrame1 = Frame(mainWindow) #Creates a frame to store widgets on in mainWindow
        MainFrame1.pack() #packs the frame
        
        EnterLabel = Label(MainFrame1, text='Enter your Maze Size:') #Creates a label that says 'Enter your Maze Size:' inside of MainFrame1
        EnterLabel.grid(row=1, column=1) #Sets the Label inside of a grid inside of MainFrame1, with the coordinates at the first row and the first column

        self.TextBox = Entry(MainFrame1) #Creates a textbox that is inside of the MainFrame1
        self.TextBox.grid(row=1, column=2) #Puts the textbox right beside of the label by putting it in a grid within MainFrame1 and have the column be 2, right next to the label

        RandomiseMazeButton = Button(MainFrame1, text='Randomise Maze', command = self.CreateMaze) #Creates the Button that has the text 'Randomise Maze', and is laced to the command of CreateMaze from a different function
        RandomiseMazeButton.grid(row=1, column=3) #Have the Button be to the right of the textbox, and within the MainFrame1 (i.e. the third column)

        FindEscapeButton = Button(MainFrame1, text='Find Escape Route', command= self.solveMaze) #Creates the button that has the text 'Find Escape Route' that finds the escape route through the solveMaze command
        FindEscapeButton.grid(row=2, column=2) # Places the Button inside of the Frame, but right in the middle of the 2nd row i.e. 2nd column
        
        self.MazeCanvas = Canvas(mainWindow, bg='White') #Creates a white canvas inside of the mainWindow
        self.MazeCanvas.pack() #places the MazeCanvas below the MainFrame1 using pack
        
        #Create Matrix Representation
        self.maze = []
        self.sol = []
        self.size = StringVar()

        mainWindow.mainloop() #runs the window
        
    def CreateMaze(self): #function that creates the maze
        self.MazeCanvas.delete('all') #Clears the Canvas
        height = self.MazeCanvas.winfo_reqheight() #gets the height of the canvas in accordance to the display
        width = self.MazeCanvas.winfo_reqwidth() #gets the width of the canvas in accordance to the display
        mazeSize = int(self.TextBox.get()) #gets the Maze Size value from the Entry widget, turns it into an integer
        self.maze = [[random.randint(0, 1) for j in range(mazeSize)] #randomises the matrix representations of each boxes later
                    for i in range(mazeSize)]
        self.maze[0][0] = 1
        
        self.squareSize = int(140/mazeSize) #sets the square size of the maze
        
        xCor = (width/2) - ((self.squareSize*mazeSize)/2) #sets the x coordinate on where it will be drawn
        yCor = (height/2) - ((self.squareSize*mazeSize)/2) #sets the y coordinate on where it will be drawn
        
        for i in range(mazeSize): #I is row
            for j in range(mazeSize): #J can be seen as a column
                if (i==0 and j==0) or (i==(mazeSize-1) and j==(mazeSize-1)): #Checks if index is the first or the last, if so, makes it green
                    self.MazeCanvas.create_rectangle((xCor+(self.squareSize*j)), (yCor+(self.squareSize*i)), ((xCor+(self.squareSize*j))+self.squareSize), ((yCor+(self.squareSize*i))+self.squareSize), fill='green', outline='black') 
                elif self.maze[i][j] == 0: #Checks if the value of the index is a 0, if so makes it gray
                    self.MazeCanvas.create_rectangle((xCor+(self.squareSize*j)), (yCor+(self.squareSize*i)), ((xCor+(self.squareSize*j))+self.squareSize), ((yCor+(self.squareSize*i))+self.squareSize), fill='gray', outline='black') 
                else: #Checks if the value of the index is a 1, if so makes it white
                    self.MazeCanvas.create_rectangle((xCor+(self.squareSize*j)), (yCor+(self.squareSize*i)), ((xCor+(self.squareSize*j))+self.squareSize), ((yCor+(self.squareSize*i))+self.squareSize), fill='white', outline='black') 
    
    def isSafe(self, maze, x, y, N): #Checks if the index is outside of the maze, returns a true if it is inside of the Maze
        if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
            return True
        return False #if it is outside, returns False
    
    def solveMazeRecur(self, maze, x, y, sol, N):
        # If (x, y is goal) return True
        if x == N - 1 and y == N - 1:
            return True
            
        if self.isSafe(maze, x, y, N) == True:
            # Check if maze[x][y] is valid
            self.sol[x][y] = 1 
            # Move forward in x direction
            if self.solveMazeRecur(maze, x+1, y, sol, N):
                return True
            # If moving in x direction doesn't give solution
            # then Move down in y direction
            if self.solveMazeRecur(maze, x, y+1, sol, N):
                return True
            
        # If the path is invalid
            # BACKTRACK: unmark x, y as part of solution path
            self.sol[x][y] = 0
            return False
    
    def solveMaze(self):
        # TODO: Create the visualization of the escape route
        mazeSize = int(self.TextBox.get())         
        height = self.MazeCanvas.winfo_reqheight()
        width = self.MazeCanvas.winfo_reqwidth()
        
        # TODO: Use list comprehension to create the matrix representation containing all 0 for the solution
        self.sol = [[0 for j in range(mazeSize)] #Sets all of the matrix representation to a 0 for all maze boxes
                    for i in range(mazeSize)]
        
        # TODO: Call the recursive function
        if self.solveMazeRecur(self.maze, 0, 0, self.sol, mazeSize) == False: #if it's 0 for any possible route, then 
            self.MazeCanvas.create_text(width/2, height-20, text="Solution doesn't exist", fill='black') #prints out a label below the maze that says 'Solution doesnt Exist' with black text
        
        # TODO: Initialize positions of x’s and y’s
        xCor = (width/2) - ((self.squareSize*mazeSize)/2)
        yCor = (height/2) - ((self.squareSize*mazeSize)/2)
        
        for i in range(mazeSize): #I is row
            for j in range(mazeSize): #J can be seen as a column
                if  self.sol[i][j] == 1: #Checks if the value of the index is a 1, if so makes it green
                    self.MazeCanvas.create_rectangle((xCor+(self.squareSize*j)), (yCor+(self.squareSize*i)), ((xCor+(self.squareSize*j))+self.squareSize), ((yCor+(self.squareSize*i))+self.squareSize), fill='green', outline='black') 
                    


MazeRunner() #runs the class