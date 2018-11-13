list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))

def find_minx(list_):
    min_elem = list_[0]
    for i in range(1, len(list_)):
        if list_[i] < min_elem:
            min_elem = list_[i]
        else: i+=1
    return min_elem

def find_maxx(list_):
    max_elem = list_[0]
    for i in range(1, len(list_)):
        if list_[i] > max_elem:
            max_elem = list_[i]
        else: i+=1
    return max_elem

print(find_maxx(list_of_nums) - find_minx(list_of_nums))

