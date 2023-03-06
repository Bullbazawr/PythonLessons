poem = input(("Введите ваш стих: ")).split()                             
dictionary_of_vowel_letters = ["у", "е", "ы", "а", "о", " э", "я", "и", "ю"]
list_of_number_vowel_letters =[]
count = 0
for i in poem:
    for j in i:
        if j in dictionary_of_vowel_letters:
            count += 1
    list_of_number_vowel_letters.append(count)
    count = 0
if list_of_number_vowel_letters[0] != 0:
    list_of_number_vowel_letters = set(list_of_number_vowel_letters)
if len(list_of_number_vowel_letters) == 1:
    print("ok")
else:
    print("not ok")