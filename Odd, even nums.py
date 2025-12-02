start_num = int(input('Enter the starting number: '))
end_num = int(input('Enter the final number: '))

print('Even numbers are equal to: ')
for i in range (start_num, end_num+1):
    if i % 2 == 0:
        print(i, end=' ')
    
print('\nOdd numbers are equal to: ')
for i in range (start_num, end_num+1):
    if i % 2 != 0:
        print(i, end=' ')