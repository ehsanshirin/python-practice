phone_book = {
    'sara': ['09011111111']
}

while True:
    menu_text = input('''
              --- دفترچه تلفن ---
1- افزودن مخاطب
2- افزودن شماره به مخاطب
3- جستجوی شماره تلفن با اسم
4- حذف مخاطب
5- تعداد مخاطبین
6- خروج
             ''')
    
    user_choice = menu_text

    if user_choice == 6 or user_choice == '':
        print('خداحافظ')
    break