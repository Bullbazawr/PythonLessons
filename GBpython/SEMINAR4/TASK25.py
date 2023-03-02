word = input("Введите строку: ")
list_1 = list(word)
print(list_1)
count = 0
many_latters =set(list_1)
print(many_latters)
for i in many_latters:
    for j in range(0, len(list_1)):
        if i == list_1[j]:
            count += 1
            if count >=2:
                list_1[j] = list_1[j] + "_" + str(count - 1)
    count = 0
for i in list_1:
    print(i, end= " ")