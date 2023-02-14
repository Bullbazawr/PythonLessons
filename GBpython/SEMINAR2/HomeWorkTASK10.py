import random
number = int(input("Enter number: "))
coin_list = []
for _ in range (number):
    coin_list.append(random.randint(0, 1))
print(coin_list)

heads = tails = 0
for coin in coin_list:
    if coin == 1:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
else:
    print(heads)