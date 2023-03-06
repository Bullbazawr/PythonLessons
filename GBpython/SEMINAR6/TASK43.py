from random import randrange
number = int(input("Enter length of first list: "))
sp1 = [randrange(15) for _ in range(number)]
count = 0
for i in range(len(sp1)):
        if sp1[i] in sp1[i+1:]:
            count += 1
print(sp1)
print(count)