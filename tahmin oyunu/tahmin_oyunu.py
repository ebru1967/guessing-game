import random

sayi = random.randint(1, 61)

print("I have chosen a number between 1 and 61. Try to guess it!")
print("You have 10 attempts.")

attempts = 10

guess = int(input("Enter your guess: "))

while attempts > 0:
    if guess == sayi:
        print("Congratulations! You guessed the number correctly.")
        break
    else:
        attempts -= 1  
        if attempts > 0:
            if guess < sayi:
                print(f"Your guess is lower than the number, please try a higher number! Remaining attempts: {attempts}")
            elif guess > sayi:
                print(f"Your guess is higher than the number, please try a lower number! Remaining attempts: {attempts}")
            guess = int(input("Enter your new guess: "))
        else:
            print("Sorry, you ran out of attempts. You couldn't guess the number.")
            break
