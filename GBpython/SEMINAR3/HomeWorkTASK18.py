len_of_list = int(input("Enter length of list: "))
find_the_number = int(input("Enter the desired number: "))
sp = []
for i in range(len_of_list):
    sp.append(i+1)
print(sp)
if find_the_number >= len_of_list:
    print(len_of_list)
else:
    print(find_the_number + 1,find_the_number -1)
