import re
word = input("Введите строку: ").upper()
word = re.findall(r'\b\w+\b', word)
word = set(word)
print(word)
print(len(word))