from random import randrange
number = int(input("Enter length of list: "))
sp = [randrange(10) for _ in range(number)]
print(sp)
unique_numbers = set(sp)
print(len(unique_numbers))