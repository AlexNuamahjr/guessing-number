import random
i = 0
while (i<=4):
  guess_number = 9
  user_input = int(input("enter guess a number(1-20) : "))
  if user_input == guess_number:
       print("you guess correct")
  else:
      print("guess is wrong")
  i = i+ 1    