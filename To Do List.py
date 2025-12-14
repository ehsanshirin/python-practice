class ToDoList:
    def __init__(self):
        self.todolist = {}
        
    def add(self):
        title = input('Title: ')
        if title in self.todolist:
            print('There is a job posted.')
            return
        
        self.title = title
        self.describt = input('Describt: ')
        self.todolist[self.title] = self.describt
        print(f'{self.title} add to list')
        
    
    def remove(self):
        self.title = input('Type Your Title: ')
        if self.title not in self.todolist.keys():
            print(f'{self.title} not find.')
            return
        self.todolist.pop(self.title)
        print(f'{self.title} remove from list')
        
        
    def done(self):
        pass

    
    def show(self):
        n = 0
        for key, value in self.todolist.items():
            n += 1
            print(f'{n}.{key}: {value}')
            
            
myList = ToDoList()
myList.add()
myList.add()
myList.remove()
myList.show()