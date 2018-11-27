string = input('Enter your word: ')
d = {}
def amount_of_each_letter(s):
    for char in s:
      d[char] = 1 + d.get(char, 0)
    return d

def is_possible_to_palindrom(d, s):
    for char in d:
        count = 0
        while d[char]%3 == 0:
            count += 1
            if count == 2:
                return 'impossible'
    d1 = amount_of_each_letter(s)
    s = list(s)
    d_keys = list(d1.keys())
    for k in d1.values():
        for i,j in zip(range(int(len(s)//2) + 1),range(int(len(d_keys)//2) + 1)):
            if k % 2 == 0:
                k1 = k//2
                while k1 != 0:
                    s[i] = s[int(len(s))-i-1] = d_keys[j]
                    k1 -= 1
                j -= k1
    return s

#print(amount_of_each_letter(string))
print(is_possible_to_palindrom(amount_of_each_letter(string),string))
