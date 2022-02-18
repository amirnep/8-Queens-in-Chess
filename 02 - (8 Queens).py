                     #This program solve 8 queens problem.

#This program is written by Mahsa Esmaeil pour.

print("The Solution Of This problem is:\n")

n = 8

def design_board(n): #This fun design our chess board 8*8.
    board = [' '] * n #8 lists design in board these are our 8 rows.
    for i in range(n):
        board[i] = [' '] * n #Every row has 8 zero or 8 column.
    return board

board = design_board(n)

N = 8

def attack(i, j):
    for k in range(0,N): #checking if there is a queen in row or column
        if board[i][k] == 'Q' or board[k][j] == 'Q':
            return False
        
    for k in range(0,N): #Check left and right diagonals.
        for l in range(0,N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 'Q':
                    return False
    return True

def queens(n):
    if n == 0: #if n is 0, solution found
        return True
    
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (attack(i,j)) and (board[i][j] != 'Q'):
                board[i][j] = 'Q'
                #Backtrack method.
                #wether we can put the next queen with this arrangment or not
                if queens(n - 1) == True:
                    return True
                
                board[i][j] = ' '

    return False

queens(N) #We call fun queens.

for i in board: #This loop is print chess board with queens.
    print (i)

print("\n")

quit = input("Press Enter to exit.") #If user press Enter, the program finished and exit.
