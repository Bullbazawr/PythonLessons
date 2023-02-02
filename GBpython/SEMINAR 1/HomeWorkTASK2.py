try:
    number = int (input('Введите число: '))
    number_for_counting_of_digits = number
    count = 1
    while number_for_counting_of_digits // 10 > 0:
        count += 1
        number_for_counting_of_digits //= 10
    sum = 0
    for i in range(count):
        sum += number % 10
        number //= 10
    print(sum)
except:
    print('Введите число!')