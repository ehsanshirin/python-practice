#Calculating the square root and cube root of a number.

import math
num = int (input ('Write a num: '))

sqr = round(math.sqrt(num),2)
cube = round(num ** (1/3), 2)

print(f'Squre {num} = {sqr}\nCube {num} = {cube}')