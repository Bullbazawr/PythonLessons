from random import randrange
number = int(input("Enter length of list: "))
sp1 = [randrange(15) for _ in range(number)]
print(sp1)
count = 0
for i in range(1, len(sp1)-1):
    if sp1[i] > sp1[i - 1] and sp1[i] > sp1[i + 1]:
        count += 1
print(count)