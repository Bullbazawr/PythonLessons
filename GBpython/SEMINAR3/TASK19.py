from random import randrange
number = int(input("Enter a number : "))
sp = [randrange(50) for i in range(10)]
print(sp)
for _ in range(number):
    sp.insert(0, sp.pop())
print(sp)
