import math

print('Enter the 3 sides of the triangle')

z1 = float(input())
z2 = float(input())
z3 = float(input())

p = (z1+z2+z3) / 2
st = math.sqrt(p*(p-z1)*(p-z2)*(p-z3))

print('Answer:', st)
