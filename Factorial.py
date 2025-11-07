n = int (input ( 'Write your number: '))
count = 0
result = 1
while count < n:
    count += 1
    result *= count
    
print(result)