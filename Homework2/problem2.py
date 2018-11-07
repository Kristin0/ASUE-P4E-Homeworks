import random

num = random.randint(1,10)
guess = input("Enter an integer: ")
if guess == "exit":
    exit(0)
counter = 0
while int(guess) != num:
    if int(guess) > num:
        guess =int(input("Enter lower: "))
        counter += 1
    elif int(guess) < num:
        guess = int(input("Enter higher: "))
        counter += 1
print("Right!It's " + str(guess) + " with " + str(counter) + "d attemp")
