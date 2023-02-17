len_of_list = int(input("Enter length of list: "))
find_the_number = int(input("Enter the desired number: "))
sp = []
for i in range(len_of_list):
    sp.append(i+1)
print(sp)
count = 0
for i in range(len_of_list):
    if sp[i] == find_the_number:
        count += 1
print(count)
