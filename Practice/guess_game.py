import random


num = random.randint(1,30)

print("Welcome to Guess me game.")
print("I am thinking of a number between 1 to 30.")
print("If your guess within 5 of my number , I'll say you are Cold.")
print("If your guess is more than  5 away from my number, I'll say you are' Warm.")
print("If your guess is farther than your most recent guess, I'll say you are getting colder.")
print("If your guess is closer than your most recent guess , I'll say you are getting Warmer.")
print("lets Play")

guesses = [0]

while True :
    guess = int(input("I am thinking of a number between 1 to 30. \n What is your guess?"))

    if guess < 1 or guess > 30:
        print("Out of Bounds , Please try again")
        continue
    # define condition to compare guess with the number
    if guess == num:
        print(f'Congratulation You have Won !!The number is {num} \nYou Guessed it in only {len(guesses)} Guesses !!')
        break
    # if guess is incorrect add guess to the guesses list for the comparison of next guess
    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("You are getting Warmer")
        else:
            print("You are getting Colder")
    else:
        if abs(num-guess) <=5:
            print("You are Warm")
        else:
            print("you are Cold")


