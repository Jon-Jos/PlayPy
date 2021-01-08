# Tic-Tac-Toe Program using random module in Python 
from random import choice

print("**********Tic-Tac-Toe Game**********")
print("***********Use Number Pad***********")
print()
# Game_board is a dictionary to store the data 
game_board = {7:' ', 8:' ', 9:' ',
              4:' ', 5:' ', 6:' ',
              1:' ', 2:' ', 3:' '}

cscore = 0 # Score of computer 
pscore = 0 # Score of player 
board = { }

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('--------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('--------')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("Computer's Score : ",cscore)
    print("Player's Score : ",pscore)

box_taken = []    # Filled spaces
box_left = [1,2,3,4,5,6,7,8,9]     # Unfilled spaces 


def box_left_func(board):
    for i in range(1,10):
        if board[i] != ' ':
            box_left.remove(i)

level=0
while(level<10):
    pmove = int(input("Make your move! \n"))
    if game_board[pmove] == ' ':
        game_board[pmove] == 'X'
        level+=1
        box_taken.append(pmove)
        box_left_func(game_board)             
        display_board(game_board)
    else:
        print("The position is already taken, make another choice : ")
        continue

    cmove = choice(box_left)
    game_board[cmove]= 'O'
    level+=1

    if level >= 5:
        #Calculating Score of Player if there is any 
        if game_board[7] == game_board[8] == game_board[9] == 'X': # across the top
             display_board(game_board)
             pscore+=1                       
        elif game_board[4] == game_board[5] == game_board[6] == 'X': # across the middle
            display_board(game_board)
            pscore+=1                
        elif game_board[1] == game_board[2] == game_board[3] != 'X': # across the bottom
            display_board(game_board)
            pscore+=1           
        elif game_board[1] == game_board[4] == game_board[7] != 'X': # down the left side
            display_board(game_board)
            pscore+=1             
        elif game_board[2] == game_board[5] == game_board[8] != 'X': # down the middle
            display_board(game_board)
            pscore+=1              
        elif game_board[3] == game_board[6] == game_board[9] != 'X': # down the right side
            display_board(game_board)
            pscore+=1       
        elif game_board[7] == game_board[5] == game_board[3] != 'X': # diagonal
            display_board(game_board)
            pscore+=1           
        elif game_board[1] == game_board[5] == game_board[9] != 'X': # diagonal
            display_board(game_board)
            pscore+=1  

         #Calculating Score of Computer if there is any 
        if game_board[7] == game_board[8] == game_board[9] == 'O': # across the top
            display_board(game_board)
            cscore+=1                       
        elif game_board[4] == game_board[5] == game_board[6] == 'O': # across the middle
            display_board(game_board)
            cscore+=1                
        elif game_board[1] == game_board[2] == game_board[3] != 'O': # across the bottom
            display_board(game_board)
            cscore+=1           
        elif game_board[1] == game_board[4] == game_board[7] != 'O': # down the left side
            display_board(game_board)
            cscore+=1             
        elif game_board[2] == game_board[5] == game_board[8] != 'O': # down the middle
            display_board(game_board)
            cscore+=1              
        elif game_board[3] == game_board[6] == game_board[9] != 'O': # down the right side
            display_board(game_board)
            cscore+=1       
        elif game_board[7] == game_board[5] == game_board[3] != 'O': # diagonal
            display_board(game_board)
            cscore+=1           
        elif game_board[1] == game_board[5] == game_board[9] != 'O': # diagonal
            display_board(game_board)
            cscore+=1     

        if pscore == 1:
            print("Player Won!")
            break
        elif csore == 1:
            print("Computer Won!")
            break
if pscore == cscore == 0:
    print("Tie!")      
yrn = input("Do you wanna play again?Y/N : ")
if yrn == 'y' or yrn =='Y':
    game()
else:
    exit  
         


# If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        
        




    




 


