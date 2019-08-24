#import module
import msvcrt
import time

name = input("Enter your name: ")

print ("Hello " +name, ', Lets play hangman.')

time.sleep (1)

print ("Start Guessing")

time.sleep(0.5)

#this is the word to be guessed
word = "secret"

#these are guesses
guesses = ""

turn = 5

while turn > 0:
     failed = 0

     for char in word:
         if char in guesses:
            print (char,end = " ")
         else:
            print ("_",end=" ")
            failed += 1

    # print ("")

     if failed == 0:
         print ("You Won")
         break

     guess = input ("Guess a charachter")

     guesses += guess

     if guess not in word:
         print ("Wrong")
         turn -= 1
         print ("You have " +str(turn), "Guesses left")

     if turn == 0:
         print ("You Lose")

