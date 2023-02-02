try:
    ticket_number = int(input("Введите номер билета: "))
    if ticket_number > 99999 and ticket_number < 1000000:
        number_a = ticket_number // 100000
        number_b = (ticket_number // 10000) % 10
        number_c = (ticket_number // 1000) % 10
        number_d = (ticket_number // 100) % 10
        number_e = (ticket_number // 10) % 10
        number_f = ticket_number  % 10
    if number_a + number_b + number_c == number_d + number_e + number_f:
        print("Удача!!! =)")
    else:
        print("Неудача =(")
except:
    print("Неверные данные!")