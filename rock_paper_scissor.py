import random 

l = ['rock','paper','scissor']

computer = l[randint(0,2)]
player = input("Enter rock/paper/scissor")


while(flag):
  if computer == player:
    print("A tie")
  elif computer == 'rock' and player == 'paper':
    print("Player Won!")
  elif computer == 'paper' and player == 'rock':
    print("Computer Won!)
  elif computer == 'paper' and player == 'scissor':
    print("Player Won!)
  elif computer == 'scissor' and player == 'paper':
    print("Computer Won!")
  elif computer == 'rock' and player == 'scissor':
    print("Computer Won!)
  else:
    print("Player Won!")
  n = input("Do you wanna hit more?Y/N)
  if n == Y and n == y:
    flag=True
  else:
    flag=False
    
 

  
 



