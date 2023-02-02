number_of_wagon = int (input('Введите номер вагона: '))
sequence_number_of_wagon = int (input('В какой вагон он сел от головы: '))
if sequence_number_of_wagon == number_of_wagon:
    print('не хватает данных!')
else:
    print('Общее количевство вагонов' + str(int(number_of_wagon) + int(sequence_number_of_wagon) - 1 ))