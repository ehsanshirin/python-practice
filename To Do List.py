class ToDoList:
    def __init__(self):
        self.todolist = {}
        
    def add(self):
        title = input('Title: ')
        if title in self.todolist:
            print('There is a job posted.')
            return
        
        
        self.describt = input('Describt: ')
        self.todolist[title] = self.describt
        print(f'{title} add to list')
        
    
    def remove(self):     
        n = 0
        for key, value in self.todolist.items():
            n += 1
            todolist = list((f'{n}.{key}: {value}'))
            todolist.append(todolist)
            print(todolist)

        title = int(input('type num from list: '))
        
        if n not in self.todolist.keys():
            print(f'{title} not find.')
            return
        
        self.todolist.pop(title)
        print(f'{title} remove from list')
        
        
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