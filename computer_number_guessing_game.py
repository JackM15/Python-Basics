import time
import random

#Welcome message for the user, delayed beteween each message.
time.sleep(3)
print("Welcome to the number guessing game.")
time.sleep(3)
print("I (your computer) will try to guess your number in less than 5 tries!")
time.sleep(5)
print("Think wisely!")
time.sleep(3)

def game():

	#ask the user for input and validate it
	try:
		userNumber = int(input("Please enter a number between 1 and 10 \n > "))
	except ValueError:
		print("You didn't enter a number")

	#computer guessing function
	def computerGuess(usersGuess):
		guessCount = 0
		pcguessedright = False

		while guessCount < 5:
			pcGuess = random.randint(1,10)
			time.sleep(3)
			print("Hmm, let me think....")
			time.sleep(4)
			print("I think your number is: {}?".format(pcGuess))
			guessCount += 1
			time.sleep(4)

			if pcGuess == userNumber:
				print("Yep, i was right!")
				pcguessedright = True
				break

		if pcguessedright == False:
			time.sleep(4)
			print("I guess you beat me, well done!")
		else:
			time.sleep(4)
			print("Victory for the computer!")
	#run computer guess
	computerGuess(userNumber)

	#give the user the option to play again
	playAgain = input("Would you like to try to beat me again? \nPlease enter \"Yes\" or \"No\"\n>")
	if playAgain.lower() != "no":
		game()

game()