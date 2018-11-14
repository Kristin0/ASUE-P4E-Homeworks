import math
num_ = int(input('Enter the number: '))


def prime_(number):
    list_ = []
    for i in range(2, number+1):
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                break
        else:
             list_.append(i)        
    return list_
print(prime_(num_))
