class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self):
        return f'{self.title} - {self.author} ({self.year})'
    
    
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f'add book {book.title}')
        
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book {title} remove')
                return
        print(f'not find {title}')
        
    def show_books(self):
        if not self.books:
            print('کتابی موجود نیست')
        else:
            print('کتاب های موجود')
            for book in self.books:
                print(book)
                
                
# نمونه استفاده
library = Library()

# اضافه کردن کتاب‌ها
library.add_book(Book("Python 101", "Michael Driscoll", 2019))
library.add_book(Book("Clean Code", "Robert C. Martin", 2008))

# نمایش کتاب‌ها
library.show_books()

# حذف یک کتاب
library.remove_book("Python 101")

# نمایش کتاب‌ها بعد از حذف
library.show_books()