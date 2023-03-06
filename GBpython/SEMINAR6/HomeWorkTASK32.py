from random import randrange
min_number = int(input("Enter min number: "))
max_number = int(input("Enter max number: "))
sp1 = [randrange(100) for _ in range(15)]
sp2 = []
for i in range(len(sp1)):
    if sp1[i] >= min_number and sp1[i] <= max_number:
        sp2.append(i)
print(sp1)
print(sp2)
