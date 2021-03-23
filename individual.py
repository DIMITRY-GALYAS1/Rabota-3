import math

print('Enter the 3 sides of the triangle')

z1 = int(input())
z2 = int(input())
z3 = int(input())

p = (z1+z2+z3) / 2
st = math.sqrt(p*(p-z1)*(p-z2)*(p-z3))

print('Answer:', st)
