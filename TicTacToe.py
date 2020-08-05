
# display the tic tac toe board
def display_board(board):
    print("\n"*100)
    print("{0:^4} | {1:^4} | {2:^4}".format(board[1], board[2],board[3]))
    print("{0:_<16}".format(""))
    print("{0:^4} | {1:^4} | {2:^4}".format(board[4], board[5],board[6]))
    print("{0:_<16}".format(""))
    print("{0:^4} | {1:^4} | {2:^4}".format(board[7], board[8],board[9]))
 
 # takes the player input
def player_input():
    player1=""
    while(player1!="X" and player1!="O"):
        player1=input("Enter marker : X or O")
       
    else:
         print("PLayer chose {}".format(player1))
        
    
    return player1       

 # assigns the respective marker to the position provided 
def place_marker(board, marker, position):
    
    board[position]=marker

 # checks for the win conditions 
def win_check(board, mark):
    
    return ((board[1]== board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) 
    or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) 
    or (board[7]==board[5]==board[3]==mark) or (board[1]==board[5]==board[9]==mark))
        

        
 # random decision of the first player
import random

def choose_first():
    c= randint(1,2)
    if c==1:
        return 1
    else:
        return 2

 
 #free space check on the position
def space_check(board, position):
    
    return board[position]==""

 # board filled or not?
def full_board_check(board):
    c=0
    for pos in board:
        if(pos==""):
            c=1
        
    return c==0        
            

 # input the position from the player
def player_choice(board):
    
    pos= int(input(("Enter the postion to be chosen as a number 1-9")))
    if space_check(board,pos)==True:
        return pos

    
 #replay 
def replay():
    
    choice=(input)("Do you want to play again: enter Y or N")
    if choice=="Y":
        return True
    else:
        return False
                   
            
  #main
 
from random import randint
print('Welcome to Tic Tac Toe!')
choice=(input)("Enter Y to play the game")
while True:
    c=0
    first=choose_first()
    print("Player {} will play first".format(first))

    second=3-first
    firstmarker=player_input()
    if firstmarker=="X":
        semarker="O"
    else:
        semarker="X"
    board=["@","","","","","","","","",""]
        
    while full_board_check(board)==False:
        display_board(board)
        print("Player {} playing...".format(first))
        firstpos=player_choice(board)
        if firstpos in range(1,10):
            place_marker(board,firstmarker,firstpos)
        display_board(board)    
        if win_check(board,firstmarker)== True :
            print("Congratulations,Player {} wins".format(first))
            c=1
            break
            
        #if win_check(board,firstmarker)== False and win_check(board,semarker)== False and full_board_check()==True:
           # print("Oops....match drew!") 
            #break   
        print("Player {} playing...".format(second))   
        secpos=player_choice(board)
        if secpos in range(1,10):
            place_marker(board,semarker,secpos)
        display_board(board)
        if win_check(board,semarker)== True :
            print("Congratulations,Player {} wins".format(second))
            c=1
            break
            
        #if win_check(board,firstmarker)== False and win_check(board,semarker)== False and full_board_check()==True:
            #print("Oops....match drew!")
            #break    
    if c==0:
      print("Oops... match drew!")    
    if not replay():
        break
        
        
    
    
