list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))

def sort(list_):                                # 4 3 1, 3 4 1, 1 3 4
    for index in range(1, len(list_)):
        value = list_[index]
        i = index - 1
        while i>=0:
            if value < list_[i]:
                list_[i+1] = list_[i]
                list_[i] = value
                i = i - 1
            else:
                break 
    return list_
    
def dif_of_list(list_):
    i = 0
    n = len(list_) - 1
    dif = list_[n] - list_[i]
    return dif

print(dif_of_list(sort(list_of_nums)))

