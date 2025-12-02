#ic = input command 
ic = input ("Write your calculation: ").split(' ')

x, op, y = float(ic[0]), ic[1], float(ic[2])

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    if x != 0 and y != 0:
        print(x / y)
else:
    print('ERROR!!\nCalculation operation not recognized.')
       

