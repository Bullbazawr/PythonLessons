sp =    [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": " S005 "},
    {" V ":" S009 "},
    {" VIII":" S007 "}
    ]
lst = []
for dict in sp:
    for v in dict.values():
        lst.append(v.strip())

lst = set(lst)
print(lst)