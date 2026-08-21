import random

number = random.randint(0, 50)

print("I have generated a number from 0 to 50.")
print("Try to guess it!")

while True:
    guess = int(input("Give me your best guess: "))

    if guess == number:
        print("You win!")
        print("The number was", number)
        break

    elif guess > number:
        print("Too high! The number is smaller.")

    else:
        print("Too low! The number is bigger.")