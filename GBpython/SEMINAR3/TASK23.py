from random import randrange
sp = [randrange(10) for _ in range(10)]
print(sp)
count = 0
for i in range(len(sp)-1):
    if sp[i] < sp[i+1]:
       count += 1
print(count)