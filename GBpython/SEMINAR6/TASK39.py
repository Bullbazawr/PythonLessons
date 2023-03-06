from random import randrange
number = int(input("Enter length of first list: "))
number2 = int(input("Enter length of second list: "))
sp1 = [randrange(15) for _ in range(number)]
sp2 = [randrange(15) for _ in range(number2)]
sp3 =[]
for i in sp1:
    if i not in sp2:
        sp3.append(i)
            
print(sp1)
print(sp2)
print(sp3)
