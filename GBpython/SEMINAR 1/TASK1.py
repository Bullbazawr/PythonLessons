import math
try:
    kilometers_per_day = int (input('Введите сколько киллометров проезжаете в день: '))
    route_length = int (input ('Введите какое расстояние нужно проехать в км.: '))
    print (math.ceil(route_length / kilometers_per_day)) 
except:
    print("Вы ввели не корректные данные!")