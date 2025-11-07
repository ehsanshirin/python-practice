n = int (input ( 'Write your number: '))
count = 0
result = 1
while count < n:
    count += 1
    result *= count
    
print(f'Factorial without Module = {result}')


# Factorial with module

import math
from math import factorial
print(f'Factorial with Module = {factorial(n)}')