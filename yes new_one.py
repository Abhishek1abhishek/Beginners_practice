from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
a =guesses_left
while guesses_left > 0:
    #to let the user input guesses
  guess = int(input("Guesses left %d: "%(a)))
  if guess == random_number:
    print ("You win!")
    break
  guesses_left -= 1
  a= a-1
else:
  print ("You lose.")
print ("The winning number is:",random_number)