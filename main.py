import math
unit = input('(L)bs or (K)g: ')
weight = int(input('Weight: '))

if unit.lower() == 'l':
    weight *= 0.45
    print(f'You are {weight} kilos')
elif unit.lower() == 'k':
    weight *= 2.21
    print(f'You are {weight} pounds')
else:
    print('Error!')
# Yayy! I officially pushed my First Python project to Github