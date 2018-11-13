num_ = int(input('Enter the number: '))


def prime_(number):
    list_ = [2,3]
    if number == 2:
        return [2]
    if number == 3:
        return list_
    for i in range(5, num_ + 1):
        if i%2!=0 and i%3!=0:
            list_.append(i)
        else:
            i+=1
    return list_
    
print(prime_(num_))
