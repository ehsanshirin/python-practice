class ToDoList:
    def __init__(self):
        self.todolist = {}
        
    def add(self):
        self.title = input('type describtion: ')
        self.describt = input('Type yore describt: ')
        self.todolist[self.title] = self.describt
        print(f'{self.title} add to list')
        
    
    def remove(self, title):
        
        print(f'{title} remove from list')

    
    def show(self):
        print(self.todolist)
        # for i in self.todolist:
        #     print(i)
            
            
myList = ToDoList()
myList.add()

myList.show()