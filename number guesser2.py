# We need to import the random number generator
from random import randint


print("Hello. Guess the right number between 1 and 10 to win!")
while True:
	compguesses = []
	# It picks a number between 1-10
	Win_number = randint(1,10)

	# We define guess as an integer. The value will be 'None'
	guess = int()
	comp_guess = int()
	#Making gameplay = True we can easily break this loop later by making it False to end t
	gameplay = True
	# We don't want the loop to start before we have an input.
	while gameplay :
		try:
	#We want a input from the user
			guess = int(input("Guess? > "))
	#We want the player to able to exit the game with ^C
		except KeyboardInterrupt:
			print("\nCtrl + C detected! Exiting...")
			exit()
	#We also want the user to type in a number and he should be informed if he types something that doesn't work.
		except:
			print("Ooops! You must type in a number")
			continue
	#Here we want to help the player by guiding them.
		if guess > Win_number:
			print("Try a lower number")
		elif guess < Win_number:
			print("Try a higher number")
	#We want the game to end by breaking this loop.
		elif guess == Win_number:
			print("That was right! you win! :)\nWould you like to play again? y/n")
			gameplay = False
			break
		while True:
			#We want the computer to learn so we take it guesses and add
			comp_guess = randint(1, 10)
			if comp_guess in compguesses:
				continue
			#Here we help the computer to guess the same we help the player to take a higher or a lower number.
			if comp_guess < Win_number:
				compguesses.extend(list(range(1,comp_guess+1)))

			if comp_guess > Win_number:
				compguesses.extend(list(range(comp_guess,11)))

			print(f"The computer guessed {comp_guess}")

			if comp_guess == Win_number:
				print("\nThe computer guessed right before you. Better luck next time...")
				gameplay = False
				break
			
			else:
				compguesses.append(comp_guess)
				
				break


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
