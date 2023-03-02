# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list()
# for i in list1:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)


# def select(f, col):
#     return[f(x) for x in col]

# def where (f, col):
#     return[x for x in col if f(x)]

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = select(int, list1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)

data = [25, 3, 4, 2, 1, 45, 64, 123, 10]
print(data)
res = list(filter(lambda x: x % 10 == 5, data))
print(res)