import math

#Uses 3.7.4 python
#returns true if solution can be found, false otherwise
#takes a two dimensional list as an input called board
def solver(solveBoard):
    boardSize = len(solveBoard) #gets size of board
    squareSize = math.floor(math.sqrt(boardSize)) #gets size of a 'cell', or the sqrt of the size of the board

    find = findEmpty(solveBoard, boardSize) #find the next empty cell
    if find: #if an empty cell is found
        row, col = find
    else: #if no empty cell is found (puzzle is solved)
        return True #base case 1, success
    #if a completed grid is submitted the program will return True, regardless of if the program is valid

    for i in range(1,boardSize+1): #for each number that could be in a cell
        if valid(solveBoard, (row, col),i,squareSize, boardSize): #attempt to see if it'd be valid if inserted
            #if it would
            solveBoard[row][col]=i #insert the number

            if solver(solveBoard): #try the 
                return True #if the success base case is hit, push it up the recursive stack

            solveBoard[row][col]=0 #otherwise remove the number
    return False; #if no number provides a valid solution, backtrack

#returns the pair (countX, countY) if a empty space can be found
#otherwise returns None
def findEmpty(findBoard, boardSize):
    for i in range(boardSize):
        for j in range(boardSize):
            if findBoard[i][j]==0:
                return (i,j)
    return None

#decides whether or not a number placement is valid.
def valid(validBoard, pos, num, squareSize, boardSize):
    #check the column and row
    for i in range(0, boardSize):
        if validBoard[pos[0]][i] == num and pos[1] != i:
            return False;
        if validBoard[i][pos[1]] == num and pos[0] != i:
            return False;
        
    x = (pos[1]//squareSize)*squareSize
    y = (pos[0]//squareSize)*squareSize
    # modulus by the sqrt of the size of the board to get a number between 0 and squareSize-1
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
