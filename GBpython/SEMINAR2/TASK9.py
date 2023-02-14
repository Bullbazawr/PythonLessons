try:
    number = int(input("Введите число: "))
    factorial_number = 1
    i = 1
    while i <= number:
        factorial_number *= i
        i += 1
    print(factorial_number)
except:
    print("error")