first_number = int(input("Enter first number: "))
division_of_numbers = int(input("Enter division of numbers: "))
number_o_sequence_elements = int(input("Enter number of sequence elements: "))
list1 = [first_number ]
i = 1
for i in range(number_o_sequence_elements):
    list1.append(first_number + (i - 1) * division_of_numbers)
    print(list1)
