a3 = int(input('Hundreds of first number - '))
a2 = int(input('Tens of first number - '))
a1 = int(input('Units of first number - '))
b2 = int(input('Tens of second number - '))
b1 = int(input('Units if second number - '))

t2 = (a1 + b1) // 10
t3 = (a2 + b2 + t2) // 10
t4 = a3 + t3
t5 = (a2 + b2 + t2) % 10
t6 = (a1 + b1) % 10

print('Numbers of sum', t4, t5, t6)
