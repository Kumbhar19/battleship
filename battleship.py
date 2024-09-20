"""""
Battleship Project
Name:Roshni Kumbhar
Roll No:2023501083
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):         
     data["rows"]= 10                                  # total count of rows in a grid
     data["col"]= 10                                   #total count of columns in a grid
     data["board_size"]= 500                           #total size of the board
     data["cell_size"]=data["board_size"]//data["rows"]# cell_size=500/10 that means each cell is 50px
     data["user_ship"]=0                               #here we assign zero ships to no.ofshipuser
     data["Computer"]=5                                #number of ships of a Computer
     data["user_board"]=emptyGrid(data["rows"], data["col"])# here we are initializing user_board as empty grid
    #  data["user_board"]=test.testGrid() 
     data["computer_board"]=emptyGrid(data["rows"], data["col"]) #here we are initializing computer_board as empty grid
     data["computer_board"]=addShips(data["computer_board"],data["Computer"])# here we add ship to the computer board by calling addship function
     data["temper_ship"]=[]                                                  #It is an temporary variable that will store user_ship data
     data["winner"]=None                                                     #It is a variable which holds as winner
     data["no_of_turns"]=50                                                  #no.of turns in a game
     data["present_number_of_turns"]=0                                       #no.of turns performed
     
    
     return 

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):                # It is view function which tells view of grid and view of the grid
    drawGrid(data,userCanvas,data["user_board"],True)      # It is view of user grid as true because the ships will be invisible on the grid
    drawGrid(data,compCanvas,data["computer_board"],False) # It is view of computer board as false because the ship will be visible on the grid
    drawShip(data,userCanvas,data["temper_ship"])          # It is to draw the temparary ships if we want
    drawGameOver(data,userCanvas)                          # It tells the game completion

    return 


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):                             #It is to track of keyboard events
    if event.keysym =="Return":                          #It checks whether key is pressed or not
        makeModel(data)                                  #It tells to restart the game                                                               
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):      #It keeps track of mouse events
    if data["winner"]==None:               #It tells us nobody has win the game
        row,col=getClickedCell(data,event) #It is used for taking the co-ordinate that is clicked on the board
        if board=="user":                  #It is used to check the click is done on user board or not                                                    
            clickUserBoard(data,row,col)   #It calls the clickuserboard and returns None                                                          
        if board=="comp":                                                                      
            if data["user_ship"]==5:       #It tells whether the five ships are placed and click is done on the computer board or not
                runGameTurn(data,row,col)  #It tells the game starts by player turn

     

#### STAGE 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):        #It creates initially as empty grid
    grid=[]                       
    for i in range(rows):                                                                         
        list=[]                  
        for j in range(cols):                                                                       
            list.append(1)                                                                               
        grid.append(list)                                                                                
    return grid  


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():                              #It creates ships for computer randomly
    ship_center_row = random.randint(1,8)      #It takes the ship's to place in row randomly by using random.randint
    ship_center_col = random.randint(1,8)      #It takes the ship's to place in col randomly by using random.randint
    k=random.randint(0,1)                 
    if k==0:                               
        return [[ship_center_row-1,ship_center_col],[ship_center_row,ship_center_col],[ship_center_row+1,ship_center_col]]
    else:                                   
        return [[ship_center_row,ship_center_col-1],[ship_center_row,ship_center_col],[ship_center_row,ship_center_col+1]]




'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):   #It check's whether the ship is placed in the grid
    for rows in ship:
        if(grid[rows[0]][rows[1]])!= EMPTY_UNCLICKED:    
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):   #  It returns the grid updated with no.ofShips added to it
    ship_count=0
    while(ship_count<numShips):
        s=createShip()
        if checkShip(grid, s):
            # ship_count=ship_count+1
            for rows in s:
                grid[rows[0]][rows[1]]=SHIP_UNCLICKED  #It iterates through each coordinates of the ship and set the grid ath the coordinate when shipis unclicked
            ship_count+=1                              #It add's 1 to present count of the ships
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips): # It draws a grid of rows and cols squares on the given canvas
        width=data["board_size"]/data["rows"]   
        height=data["board_size"]/data["rows"]
        for row in range(data["rows"]):
            for col in range(data["col"]):
                a1=col*width
                b1=row*height
                a2=(col+1)*width
                b2=(row+1)*height
                if grid[row][col]==SHIP_UNCLICKED and showShips==True: #In this it checks for row and col whether ship is unclicked and showships is true then the color will be yellow
                    color="yellow"
                elif grid[row][col]==EMPTY_UNCLICKED:
                    color="blue"
                elif grid[row][col]==SHIP_CLICKED:
                    color="red"
                elif grid[row][col]==EMPTY_CLICKED:
                    color="white"
                elif showShips==False and grid[row][col]==SHIP_UNCLICKED :
                        color="blue"       
                canvas.create_rectangle(a1,b1,a2,b2,fill=color)        
        return


### STAGE 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):   #It takes in a ship and returns True if the ship is placed vertically otherwise it is false
    ship.sort()
    for row,col in ship:
        if ship == [[row-1,col],[row,col],[row+1,col]]:
            return True
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship): # It takes in a ship and return True if the ship is placed horizontally otherwise False
    ship.sort()
    for row,col in ship:
        if ship ==[[row,col-1],[row,col],[row,col+1]]:
            return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):  #It detect where a user has clicked on the board
    cellsize=data["cell_size"]
    X=int(event.y//cellsize)      #It takes x and y coordinates of each cellsize
    Y=int(event.x//cellsize)
    return [X,Y]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):   #It draws the cells for each component for the given ship
    for row in range(data["rows"]):
        a1=row*data["cell_size"]    #It takes the each cell size of top row
        b1=a1+data["cell_size"]     #It takes the each cell size of bottom =top(each index value)
        for col in range(data["col"]):
            a2=col*data["cell_size"]
            b2=a2+data["cell_size"]

            if[row,col] in ship:
                color="white"

                canvas.create_rectangle(a2,a1,b2,b1,fill=color)  


    return None


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):#It determines whether it is legal to place the ship on the grid and returning a boolean
    if len(ship)!=3:
        return False
    for i in ship:
        row, col = i
        if grid[row][col]== SHIP_CLICKED:
            return False
    if not ((checkShip(grid,ship)) and (isHorizontal(ship) or isVertical(ship))) :
        return False

    return True


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):# It takes the data model  and checks if the current temporary ship is valid or not
    if shipIsValid(data["user_board"],data["temper_ship"]):#It tell if the ship is valid it place it on the user board
        data["user_ship"]+=1
        for b in data["temper_ship"]:
            row,col=b
            data["user_board"][row][col]=SHIP_UNCLICKED
    else:
        print("Invalid ship")  # IF it is not valid
    data["temper_ship"]=[]           
    
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col): #It row and col  to update the temporary ship and board
    if data["user_ship"]==5:        #Here we assigning user_ship only five
        return
    if[row,col] in data["temper_ship"]:
        return
    

    data["temper_ship"].append([row,col])
    if len(data["temper_ship"])==3:
        placeShip(data)
    if data["user_ship"]==5:
        print("Start the game")
        return  
    


### STAGE 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player): # Here which updates the given board at row and col based on a player's click
    if board[row][col]==SHIP_UNCLICKED:         #If user clicks on cell with value ship-unclicked and the board will update that cell to intead be ship clicked
        board[row][col]=SHIP_CLICKED
        if isGameOver(board):
            data["winner"]=player
    elif board[row][col]==EMPTY_UNCLICKED:      #If the user clicks on a cell with value Empty unclicked and it should update to be empty clicked
        board[row][col]=EMPTY_CLICKED           

    
        
    return None


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col): # It manages a single turn of the game after a user clicks on row and col
    if data["computer_board"][row][col]==SHIP_CLICKED or data["computer_board"][row][col]==EMPTY_CLICKED:
        return None
    else:
        updateBoard(data, data["computer_board"], row,col ,"user")
    [row,col]=getComputerGuess(data["user_board"])
    updateBoard(data,data["user_board"],row,col,"comp") # It tell cell has not been click before then it call updateBoard with parameter as user as the player
    data["present_number_of_turns"]+=1
    if data["present_number_of_turns"] > data["no_of_turns"]:
        data["winner"]="draw"
    return None


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board): #It tell the computer to make a guess as well
    while True:
        row=random.randint(0,9) # It is used to pick the row and col for select cells randomly
        col=random.randint(0,9)
        if board[row][col]!=EMPTY_CLICKED and board[row][col]!=SHIP_CLICKED:
            return [row,col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board): # It checks whether the game is over for the given board
    for col in board:
        for c in col:
            if c== SHIP_UNCLICKED:#The game is done if there are no ship unclicked 
                return False      # It return True if the game is over for the board and False otherwise

    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas): # It showns a special message on the given canvas if a winner has been chosen
    if data["winner"]=="user":
        canvas.delete("all")
        canvas.create_text(250,250,text="congratulations",fill="red")
        canvas.create_text(290,290,text="press the Enter key to play again",fill="red")
    elif data["winner"]=="Comp":
        canvas.delete("all")
        canvas.create_text(250,250,text="You lost the game",fill="red")
        canvas.create_text(290,290,text="press the Enter key to play again",fill="red")
    if data["winner"]=="draw":
        canvas.delete("all")
        canvas.create_text(250,250,text="Out of moves",fill="red")
        canvas.create_text(290,290,text="press the Enter key to play again",fill="red")

    return

### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":


    print("\n" + "#"*15 + " STAGE 1 TESTS " +  "#" * 16 + "\n")
    test.stage1Tests()

    ## Uncomment these for STAGE 2 ##
    
    print("\n" + "#"*15 + " STAGE 2 TESTS " +  "#" * 16 + "\n")
    test.stage2Tests()
    

    ## Uncomment these for STAGE 3 ##
    
    print("\n" + "#"*15 + " STAGE 3 TESTS " +  "#" * 16 + "\n")
    test.stage3Tests()
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
