import random

num = random.randint(1,10)
guess = input("Enter your number: ")
counter = 0
while guess != "exit" and int(guess) != num:
    if int(guess) > num:
        guess = input("Enter lower: ")
        counter += 1
    elif int(guess) < num:
        guess = input("Enter higher: ")
        counter += 1
if guess == "exit":
    print("Exit")
else:
    print("Right!It's " + str(guess) + " with " + str(counter) + "d attemp")                                                       
                  


