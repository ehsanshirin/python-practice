def add_note():
    note = input('add your note: ')
    with open('notebook.txt', 'a') as f:
        f.write(note + '\n')
        
def view_note():
    with open('notebook.txt' , 'r') as f:
        notes = f.readlines()
    for i, note in enumerate(notes, 1):
        # با شماره‌گذاری از 1 به بالا، یادداشت‌ها را چاپ می‌کند.
        print(f'{i}. {note}', end='')
        # هر یادداشت را با شماره آن چاپ می‌کند.
        # باعث می‌شود که دستور پرینت خودش خط جدید اضافه نکند ،end=''
        # چون یادداشت‌ها از قبل با"اسلش ان" پایان یافته‌اند
        
while True:
    print('\n1: add new note\n2: View Nots\n3: Exit')
    
    choise = input('Your Choise: ')
    
    if choise == '1':
        add_note()
    elif choise == '2':
        view_note()
    elif choise == '3':
        break
    else:
        print('Error')