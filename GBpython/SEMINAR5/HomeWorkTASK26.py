def rec(number, number1):
    if number1 == 0:
        return 1
    else:
        return number * rec(number, number1 -1)

number = int(input("Enter first number: "))
number1 = int(input("Enter second number: "))

print(rec(number, number1))