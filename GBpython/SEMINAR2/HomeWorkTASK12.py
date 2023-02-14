from cmath import sqrt
sum = int(input("Enter sum of numbers: "))
multiplication = int(input("Enter multiplication of numbers: "))
d = sum**2 - multiplication*4
if d < 0:
    print("There is no solution.")
elif d > 0:
    x = (sum + sqrt(d)) / 2
    y = (sum - sqrt(d)) / 2
else:
    x = y = int(multiplication / 2) 
print(int(x.real), int(y.real))
