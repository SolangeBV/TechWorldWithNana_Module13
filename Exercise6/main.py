import random

print("Hi there! This program will generate a random number between 1 and 9 and you will have to guess it.")
random_number = random.randint(1,9)
while True:
  user_input = input("Enter a number: ")
  guessed_number = int(user_input)
  if guessed_number == random_number:
    print("YOU WON!")
    break
  elif guessed_number < random_number:
    print("Your guess is too low.")
  else:
    print("Your guess is too high.")
