  1 import random
  2 
  3 num = random.randint(1,10)
  4 guess = input("Enter an integer: ")
  5 counter = 0
  6 while int(guess) != num:
  7     if guess == "exit":
  8         exit(0)
  9     elif int(guess) > num:
 10         guess = (input("Enter lower: "))
 11         counter += 1
 12     elif int(guess) < num:
 13         guess = (input("Enter higher: "))
 14         counter += 1
 15 #    elif guess == "exit":
 16 #        break
 17 print("Right!It's " + str(guess) + " with " + str(counter) + "d attemp")

