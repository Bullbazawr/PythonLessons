from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
square_of_elips = list(map(lambda ell : pi * ell[0] * ell[1], orbits))
print(square_of_elips)
find_farthest_orbit = lambda x : x.index(max(x))
print(find_farthest_orbit(square_of_elips))