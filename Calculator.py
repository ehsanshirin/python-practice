def sum_num():
    pass

#ic = input command 
ic = input ("Write your calculation: ").split(' ')
tmp_num = 0
for i in ic:
    if i.isdigit():
        print('ok', i)
        
        tmp_num = int(i)
    else:
        print('no', i)
        if i == '+':
            
            
    

# def sum_num():
#     pass

