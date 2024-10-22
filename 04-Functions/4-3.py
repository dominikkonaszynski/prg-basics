###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
s = int((a+b+c)/2)
def triangle_area(a,b,c):
    result = math.sqrt(s * ((s-a)*(s-b)*(s-c)))
    return result

area = triangle_area(a,b,c)
print(f'The area of ​​a triangle with sides {a}, {b} and {c} is {area} ')