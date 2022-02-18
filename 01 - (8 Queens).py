                      #8 Queens problems in python

#This program is print solutions of 8 queens problem in chess.
#This is written by Amir Nematpour
#Let's start:

import copy #For copy answers in our list.

n = 8 #We write this program for 8*8 board.
def chessboard(n): #This fun design our chess board.
    board = ['.'] * n #8 lists every board has 8 indexs that is design our 8*8 board.
    for x in range(n): #We type a loop for desgin 8*8 board.
        board[x] = ['.'] * n
    return board

def printf(sol,n): #Print our sols with this fun.
    for i in sol: #This loop is for indexs of list sol.
        for j in i: #Every index in list sol has 8 list(rows).
            print(j) #Print every rows with 8 columns.
        print("-----------------------------------------") #
        
def safe(board,row,column,n): #This fun use for safe place in board to replace queens.
    for y in range(column): #Replace first queen and replace zero in row.
        if board[row][y] == 'Q': #If in row and column y we have queen this fun return false.
            return False

    x,y = row,column #Replace row in x and column in y.

    while x >= 0 and y >= 0: #This loop is for replace 0 in left corner of each queen.
        if board[x][y] == 'Q': #If in row x and column y we have queen this fun return false.
            return False
        x -= 1 #Use for find left corner.
        y -= 1 #Use for find left corner.

    jx,jy = row,column #Replace row in jx and column in jy.

    while jx < n and jy >= 0: #This loop is for replace 0 in right corner of each queen.
        if board[jx][jy] == 'Q': #If in row jx and column jy we have queen this fun return false.
            return False
        jx += 1 #Use for find left corner.
        jy -= 1 #Use for find left corner.

    return True #If this fun doesn't return false it's return true.

def solve(board,column,n): #This fun for solve the problem.
    for i in range(n):
        if safe(board,i,column,n): #Goto safe fun to know if is safe or not??
            board[i][column] = 'Q' #If fun safe is true replace 1.
            if column == n - 1: 
                add(board) #To add answers in list sol.
                board[i][column] = '.' 
                return
            solve(board,column+1,n) #Backtrack method to solve the problem.
            board[i][column] = '.'

def add(board): #Add answers to list sol.
    s = copy.deepcopy(board) #Copy board in s.
    sol.append(s) #Append s in sol list to print.

board = chessboard(n) #Replace chessboard fun in board.

sol = [] #Sol list to save our solutions.

solve(board,0,n) #Use solve fun for n=8.

printf(sol,n) #Print all solutions.

print("Count of answers are:",len(sol)) #Print count of solutions.

quit = input() #Press any key to quit program.
