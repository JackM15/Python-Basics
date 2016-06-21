import random

# generate a random number between 1 and 10
secretNumber = random.randint(1,10)

def game():
  guesses = 0
  while True:
    # get a number guess from the player, if it's not a number, tell them and ask again.
    while True:
      try:
          guess = int(input("Guess a number between 1 and 10 \n"))
          break
      except ValueError:
          print("You didn't enter a number!")
          guesses += 1
          print("You have used {}/5 guesses.".format(guesses))
    
    #Give the user 5 guesses to do it!
    if guesses < 5:
      # compare guess to secret number, if it matches then break, if not tell them they're wrong.
      if guess == secretNumber:
          guesses += 1
          print("-" * 30)
          print("You got it, my number was {}.".format(secretNumber))
          print("It took you: {} tries to guess.".format(guesses))
          print("-" * 30)
          #reset guesses to 0
          guesses = 0
          break
      #print hit or miss
      elif guess <= 0:
          print("That number is less than 1, try again!")
          guesses += 1
          print("You have used {}/5 guesses.".format(guesses))
      elif guess >= 11:
          print("That number is higher than 10, please try again!")
          guesses += 1
          print("You have used {}/5 guesses.".format(guesses))
      else:
          print("That's not it!")
          print("Try guessing again!")
          guesses += 1
          print("You have used {}/5 guesses.".format(guesses))
    #Break out of the loop if they took too long.
    else:
      print("You took too many times to guess, my number was: {}.".format(secretNumber))
      break

  #ask user if they want to play again    
  playAgain = input("Do you want to play again? - Y/n \n > ")
  #if its not n, play again.
  if playAgain.lower() != 'n':
    game()

#Run game
game()