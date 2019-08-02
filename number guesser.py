print("Hello, guess the right number between 1 and 10 to win!")
#We need to import the random number generator
from random import randint
#It picks a number between 1-10
Win_number = randint(1,10)
#We ask with a input whats your number.
message = "what is your guess?"
guess = int(input(message))
#We don't want the loop to start before we have an input.
if guess != None:
	while guess != Win_number:
		if guess > Win_number:
			message = "Try a lower number"
		elif guess < Win_number:
			message = "Try a higher number"
		guess = int(input(message))
	else:
		print("That was right! you win! :)")
		exit()
		
