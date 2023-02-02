try:
    number_of_origami = int(input("Введите общее ко-во  журавликов: "))
    if number_of_origami % 6 == 0:
        peter = number_of_origami // 6
        kate = (peter + peter) * 2
        print("Катя сделала", kate)
        print("Сережа сделал", peter)
        print("Петя сделал", peter)
    print("Они не могли столько сделать")
except:
    print("Неверные данные")
