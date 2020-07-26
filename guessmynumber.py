import math
import random
import time 

print("Welcome to the Guess the Number Game! \nThe goal of the game is to guess the number I am thinking!")
choice = input("Do you want to play? Enter 'No' to quit and 'Yes' to play!")

if choice=="No":  
    print("Ok! Have a good day!")
    exit()
else:
    print("You have chosen to play!\nThink of a number between 0 and 100!")

totalguesses = 0
number = random.randrange(0, 101, 2) 
guess = -1
while (guess != number):
    while True:
        try:
            guess = int(input("Enter your guess!"))
            break
        except:
            print("That's not a valid number!")
    if(guess > number):
        print("Hey! The number I am thinking is lower than that!!!")
        totalguesses = totalguesses + 1
    elif(guess < number):
        print("Hey! The number I am thinking of is high than that!!")
        totalguesses = totalguesses + 1

if (totalguesses == 1):
    print("How in the world did you do that huh?")
else:
    print("Only took you {} guesses to guess the number!".format(totalguesses))