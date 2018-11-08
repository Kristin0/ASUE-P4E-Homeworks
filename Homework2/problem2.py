  1 import random
  2 
  3 num = random.randint(1,10)
  4 guess = input("Enter your number: ")
  5 counter = 0
  6 while guess != "exit" and int(guess) != num:
  7     if int(guess) > num:
  8         guess = input("Enter lower: ")
  9         counter += 1
 10     elif int(guess) < num:
 11         guess = input("Enter higher: ")
 12         counter += 1
 13 if guess == "exit":
 14     print("Exit")
 15 else:
 16     print("Right!It's " + str(guess) + " with " + str(counter) + "d attemp")
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
                  


