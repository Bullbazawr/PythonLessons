try:
    chocolate_bar_lenght = int(input("Введите количество плиток в длину: "))
    chocolate_bar_width = int(input("Введите количество плиток в ширину: "))
    get_chocolate_size = int(input("Сколько плиток вы хотите получить?: "))
    if get_chocolate_size % chocolate_bar_lenght == 0 and get_chocolate_size <= chocolate_bar_lenght * chocolate_bar_width:
        print("У вас получится!")
    else:
        print("Так не выйдет!")
except:
    print("Неверные данные")