import random

iterations = int(input("Iterations quantity: "))
win_when_switching = 0
win_when_not_switching = 0



for x in range(iterations):
    host_choice = random.randint(1,3)
    prize_door = random.randint(1,3)
    cont_num = random.randint(1,3)
    switched_door = random.randint(1,3)
    while (host_choice == cont_num or  host_choice == prize_door):
         host_choice = random.randint(1,3)
    
    print("Prize is behind " + str(prize_door))    
    print("Host door: " + str(host_choice))
    print("Contestant chooses door " + str(cont_num))
    switching = random.randint(0,1)
    if switching == 0:
        print("Contestant doesn't switch the door")
        if cont_num == prize_door:
            print("Contestant Won!\n")
            win_when_not_switching += 1
        else:print("Contestant Lost!\n")
    elif switching == 1:
        while (switched_door == cont_num or switched_door == host_choice):
            switched_door = random.randint(1,3)
        print("Contestant switches from door " + str(cont_num) + " to "+\
            str(switched_door))
        if switched_door == prize_door:
            print("Contestant Won!\n")
            win_when_switching += 1
        else: print("Contestant Lost!\n")

percent_if_switching = (win_when_switching/iterations)*100
percent_if_not_switching = (win_when_not_switching/iterations)*100
print("Probability of winning when swtiching: " + str(percent_if_switching)+"%")
print("Probabilty of winning when NOT switching: " + str(percent_if_not_switching) + "%")
