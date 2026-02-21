my_friends = {
    'ali': 10,
    'hasan': 20,
    'hosein': 30
}

while True:
    get_name = input('type name your frinds: ').strip().lower()
    
    if get_name == 'exit':
        print('Goodbye!')
        break
    
    if get_name in my_friends:
        try:
            age_guess = int(input(f"How Much Age's {get_name}: "))
            real_age = my_friends[get_name]
            
            while age_guess == real_age:
                
                if age_guess < real_age:
                    print('is Low, Try again: ')
                    
                elif age_guess > real_age:
                    print('is big, try again: ')
                                        
                else:
                    print('is Good')
                    break
                    

        except ValueError:
            print('Type Only Number!')

    else:
        print('Not Find, Try again')
    
    print('_'*30)
