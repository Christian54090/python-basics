i = 1
while i <= 5:
    print(i)
    i += 1

# Guessing Game
correct_number = 13
guess = input("Guess a number between 1 - 20: ")
guesses = 1
while int(guess) != correct_number and guesses <= 3:
    guesses += 1
    guess = input("Wrong! Guess another number: ")

if int(guess) == correct_number:
    print("Congrats! You guessed right!")
