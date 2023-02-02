import math
first_class_quantity = int(input("Введите кол-во учеников в первом классе: "))
second_class_quantity = int(input("Введите кол-во учеников в втором классе: "))
third_class_quantity = int(input("Введите кол-во учеников в третьем классе: "))

if first_class_quantity % 2 == 0:
    the_required_number_of_desks_first = int (first_class_quantity / 2)
else:
    the_required_number_of_desks_first = int (math.ceil(first_class_quantity / 2))
if second_class_quantity % 2 == 0:
    the_required_number_of_desks_second = int (second_class_quantity / 2)
else:
    the_required_number_of_desks_second = int (math.ceil(second_class_quantity / 2))
if third_class_quantity % 2 == 0:
    the_required_number_of_desks_third = int (third_class_quantity / 2)
else:
    the_required_number_of_desks_third = int (math.ceil(third_class_quantity / 2))
total_quantity_of_desks = the_required_number_of_desks_first + the_required_number_of_desks_second + the_required_number_of_desks_third
print (total_quantity_of_desks)