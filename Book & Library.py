class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = [] #book List
    
    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" add to library')
    
    def book_list(self):
        if not self.books:
            print('No Books in library')
            return
        
        for b in self.books:
            if b.is_borrowed:
                status = 'Borrowed'
            else:
                status = 'Available'
            
            print(f'{b.title} by {b.author} - {status}')
    
    def borrowed(self, title):
        for b in self.books:
            if b.title == title:
                if b.is_borrowed:
                    print('Already borrowed')
                else:
                    b.is_borrowed = True
                    print(f'You borrowed: {title}')
                return
            
        print('Book not found')
    
    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                if not b.is_borrowed:
                    print('This book was not borrowed')
                    
                else:
                    b.is_borrowed = False
                    print(f'You returned: {title}')
                return
        print('Book not found')
        
        
b1 = Book('python 101', 'Mike')
b2 = Book('AI Basics', 'John')
b3 = Book('Data Science', 'Sara')


lib = Library()


lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)


lib.book_list()


lib.borrowed('Python 101')

lib.book_list()

lib.return_book('Python 101')

lib.book_list()