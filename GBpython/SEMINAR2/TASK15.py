import random
number = int(input("Enter number: "))
watermelon_list = []
for _ in range (number):
    watermelon_list.append(random.randint(5, 15))
print(watermelon_list)

max_weight = min_weight = watermelon_list[0]
for weight in watermelon_list:
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
print(max_weight)
print(min_weight)