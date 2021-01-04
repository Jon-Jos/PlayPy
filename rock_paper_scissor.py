from random import randint

l = ['rock','paper','scissor']
flag = True
while(flag):
  computer = l[randint(0,2)]
  player = input("Enter rock/paper/scissor:\t")
  print("Computer : \t",computer)
  print("Player : \t",player)
  if computer == player:
    print("A tie")
  elif computer == 'rock' and player == 'paper':
    print("Player Won!")
  elif computer == 'paper' and player == 'rock':
    print("Computer Won!")
  elif computer == 'paper' and player == 'scissor':
    print("Player Won!")
  elif computer == 'scissor' and player == 'paper':
    print("Computer Won!")
  elif computer == 'rock' and player == 'scissor':
    print("Computer Won!")
  else:
    print("Player Won!")
  
  N = str(input("Do you wanna hit more?Y/N:\t"))
  if N == 'Y' or N == 'y':
    flag=True
  else:
    flag=False
    
 

  
 



