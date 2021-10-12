import math

# Uses 3.7.4 python
# returns true if solution can be found, false otherwise
# takes a two dimensional list as an input called board
# Uses a depth first search
def solver(solveBoard):
    # gets size of board
    boardSize = len(solveBoard) 
    # gets size of a 'cell', or the sqrt of the size of the board
    squareSize = math.floor(math.sqrt(boardSize)) 

    # find the next empty cell
    find = findEmpty(solveBoard, boardSize) 
    # if an empty cell is found
    if find: 
        row, col = find
    # if no empty cell is found (puzzle is solved)
    else: 
        # base case 1, success   
        return True 
    # if a completed grid is submitted the program will return True,
    # regardless of if the program is valid
    
    # for each number that could be in a cell
    for i in range(1,boardSize+1): 
        # attempt to see if it'd be valid if inserted and if it would be
        if valid(solveBoard, (row, col),i,squareSize, boardSize): 
            # insert the number
            solveBoard[row][col]=i 
            if solver(solveBoard): #try the 
                # if the success base case is hit, 
                # push it up the recursive stack
                return True 
            # otherwise remove the number
            solveBoard[row][col]=0 
    # if no number provides a valid solution, backtrack
    return False; 

# returns the pair (countX, countY) if a empty space can be found
# otherwise returns None
def findEmpty(findBoard, boardSize):
    for i in range(boardSize):
        for j in range(boardSize):
            if findBoard[i][j]==0:
                return (i,j)
    return None

# decides whether or not a number placement is valid.
def valid(validBoard, pos, num, squareSize, boardSize):
    # check the column and row
    for i in range(0, boardSize):
        if validBoard[pos[0]][i] == num and pos[1] != i:
            return False;
        if validBoard[i][pos[1]] == num and pos[0] != i:
            return False;
        
    x = (pos[1]//squareSize)*squareSize
    y = (pos[0]//squareSize)*squareSize
    # modulus by the sqrt of the size of the board to get a
    # number between 0 and squareSize-1
    # multiply by 3 to get 0, 3 or 6. Giving the squares starting positions
    for i in range(y,y+squareSize):
        for j in range(x,x+squareSize): #check the cell
            if (validBoard[i][j]==num and (i,j)!=pos):
               return False;
    return True;

board = [[1,2,3,4,5,6,7,8,9],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
board2 = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         ]
solver(board2)
for i in board2:
    print(i)
#Improvements
    #Able to submit your own grid
    #Make a GUI
    #Textually show the program running
