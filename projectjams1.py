#project:
#randomly pick a number from 0-9 and ask the user to guess the number
#tell them if their guess is too high or too low if they are wrongcle
#tell them they're correct and end the loop if they guess correctly
#error checking

import random

randomnumber = random.randint(1, 10)

print(randomnumber)

guess = int(input ("guess the correct random number between 1 to 10\n"))


while guess != randomnumber:
    if guess < randomnumber:
        print("too low")
    if guess > randomnumber:    
        print("too high")
    guess = int(input("guess again nerd\n"))



print("nice \n")

#else:
 #   guess = int(input ("\nGUESS AGAIN NERD\n"))



    #if guess == randomnumber:
      #  print ("\n nice \n")






#while randomnumber = guess
   # print = ("Nice.")
    #else:
     #   print ("guess again")