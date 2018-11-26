cache = {}
def factorial(n):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = n*factorial(n-1)
    return cache[n]

i = int(input('Enter the num: '))
print(factorial(i))
i = int(input())
print(factorial(i))
#print(cache)
