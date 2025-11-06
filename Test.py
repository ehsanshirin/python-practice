# num = int (input('write a num: '))

# if num <= 1:
#     print(f'{num} is not prime')
# else:
#     for i in range (2, int(num ** 0.5)+1):
#         if num % i == 0:
#             print(f'{num} is not prime')
#             break
#         else:
#             print(f'{num} is prime')
#             break


for w in "hello4444wsnsch":
    # if w.isdigit():
    #     print(w)
    
    try:
        print(int (w))
    
    except:
        print('is not digit', w)