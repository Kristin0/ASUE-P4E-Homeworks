import random

your_number = int(input("Enter the door number: "))
prize_door = random.randint(1,3)

print("Prize is behind door " + str(prize_door))
print("Contestant chooses door " + str(your_number))

if  prize_door == 1:
    host_choose = random.randint(2,3)
elif prize_door == 2:
    host_choose = random.choice([1,3])
else:   
    host_choose = random.choice([1,2])

print("Host opens door " + str(host_choose))
your_choice = int(input("If you want to switch the door, write a number\
        or 0: "))
if str(your_choice) != 0:
    print("Contestant swithces from door " + str(your_number) + " to"\
           + str(your_choice))
else:
    print("Contestant doesn't switch the door")

if your_number == prize_door:
    print("Contestant won!")
else:
    print("Lost")
