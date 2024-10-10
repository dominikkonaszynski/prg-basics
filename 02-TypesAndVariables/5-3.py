cuboid_side_string_a = input('Enter cuboid side a: ')
a = int(cuboid_side_string_a)
cuboid_side_string_b = input('Enter cuboid side b: ')
b = int(cuboid_side_string_b)
cuboid_side_string_c = input('Enter cuboid side c: ')
c = int(cuboid_side_string_c)
cuboid_volume = a * b * c
cuboid_surface_area = 2 * (a*b + b*c + a*c)
print(f'The volume of a cuboid with sides of {a}, {b} and {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides of {a}, {b} and {c} is {cuboid_surface_area}')

