my_friends = {
    'ali': 10,
    'hasan': 20,
    'hosein': 30
}

get_name = input('type name your frinds: ')
age_person = int(input('type his age: '))

while True:
    if my_friends.get(get_name):
        while age_person == my_friends[get_name]:
            print('gooood')
            # if age_person < my_friends[get_name]:
            #     print('عدد کوچک هست')
            # else:
            #     print('عدد زیاد هست')
    else:
        print('no')
        pass