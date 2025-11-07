def sum_nums(nums):
    print(sum(nums))

def minus_nums(nums):
    pass

import math
from math import prod
def multiply(nums):
    print(math.prod(nums))
    
def sum_nums(nums):
    print(sum(nums))
     
#ic = input command 
ic = input ("Write your calculation: ").split(' ')
nums = []
for i in ic:
    if i.isdigit():
        nums.append(int(i))
    
for i in ic:
    if i == '+':
        sum_nums(nums)
    if i == '-':
        pass
    if i == '*':
        multiply(nums)
    if i == '/':
        pass    

# else:
#         print('''ERROR!!\nCalculation is not possible!''')
#         break