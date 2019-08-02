
# We need to import the random number generator
from random import randint

print("Hello. Guess the right number between 1 and 10 to win!")
while True:
	
	# It picks a number between 1-10
	Win_number = randint(1,10)

	# We define guess as an integer. The value will be 'None'
	guess = int()

	# We don't want the loop to start before we have an input.
	while guess != Win_number:
		try:
			guess = int(input("Guess? > "))
		except KeyboardInterrupt:
			print("\nCtrl + C detected! Exiting...")
			exit()
		except:
			print("Ooops! You must type in a number")
			continue

		if guess > Win_number:
			print("Try a lower number")
		elif guess < Win_number:
			print("Try a higher number")
		else:
			print("That was right! you win! :)\nWould you like to play again? Y/N")
	while True:
		try:

			
			Play_again = input("Play again? y/n:")
		except KeyboardInterrupt:
			print("\nCtrl + C detected! Exiting...")
			exit()
		if Play_again == "y":
			print("Guess the number again!")
			break
		
		elif Play_again == "n":
			print("Thanks for playing! :)")
			exit()
		else:
			print("Invalid answer")
