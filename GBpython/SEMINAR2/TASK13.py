import random

number = int(input("Enter number: "))
flag = True
while flag:
    if number < 1 or number > 99:
        print("Error number!")
        number = int(input("Enter number: "))
    else:
        flag = False

temp_stat = []

for _ in range(number):
    temp_stat.append(random.randint(-50, 50))
print(temp_stat)
count = max_count = 0
for temp in temp_stat:
    if temp > 0:
        count += 1
        if max_count < count:
                max_count = count
    else:
        count = 0
print(max_count)