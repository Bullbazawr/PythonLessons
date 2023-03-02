def sum_of_numbers(number1, number2):
    if not number2:
        return number1
    return sum_of_numbers(number1 + 1, number2 - 1)


print(sum_of_numbers(13, 72))
