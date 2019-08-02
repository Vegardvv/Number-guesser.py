
# We need to import the random number generator
from random import randint

print("Hello. Guess the right number between 1 and 10 to win!")

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
		break
	except:
		print("Ooops! You must type in a number")
		continue

	if guess > Win_number:
		print("Try a lower number")
	elif guess < Win_number:
		print("Try a higher number")
	else:
		print("That was right! you win! :)")
		break # Instead of 'exit()', you can break the while loop by using 'break'
