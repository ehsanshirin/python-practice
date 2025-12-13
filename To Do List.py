class ToDoList:
    def __init__(self):
        self.todolist = {}
        
    def add(self, title):
        self.todolist[title] = input('type describtion: ')
        
        print(f'{title} add to list')
        
    
    def remove(self, title):
        
        print(f'{title} remove from list')

    
    def show(self):
        print('Your List: ')
        for i in self.todolist:
            print(i)
            
            
myList = ToDoList()
myList.add('Python')

myList.show()