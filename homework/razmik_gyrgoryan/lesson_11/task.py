class Books:
    have_text = True

    def __init__(self, name_book, author, pages, material, flag, isbn):
        self.name_book = name_book
        self.author = author
        self.pages = pages
        self.material = material
        self.flag = flag
        self.isbn = isbn

    def print_books(self):
        print(f'Название: {self.name_book}, Автор: {self.author}, страниц: {self.pages}, '
              f'материал: {self.material}, зарезервирована' if self.flag else
              f'Название: {self.name_book}, Автор: {self.author}, '
              f'страниц: {self.pages}, материал: {self.material}')


first_book = Books("Идиот", "Достоевский", 500, "бумага", True, 1234)
second_book = Books("Идиот", "Достоевский", 500, "бумага", False, 4545)
third_book = Books("Идиот", "Достоевский", 500, "бумага", False, 6767)
fourth_book = Books("Идиот", "Достоевский", 500, "бумага", False, 8976)
fives_book = Books("Идиот", "Достоевский", 500, "бумага", False, 7878)


class ClassBooks(Books):
    tasks = True

    def __init__(self, name_book, author, pages, flag, isbn, material, subject, school_class):
        super().__init__(name_book, author, pages, material, flag, isbn)
        self.subject = subject
        self.school_class = school_class

    def print_books(self):
        print(f'Название: {self.name_book}, Автор: {self.author}, страниц: {self.pages}, '
              f'предмет: {self.subject}, класс: {self.school_class}, зарезервирована' if self.flag else
              f'Название: {self.name_book}, Автор: {self.author}, '
              f'страниц: {self.pages}, предмет: {self.subject}, класс: {self.school_class}')


class_book_first = ClassBooks("Алгебра", "Иванов", 200, False, 123123, "бумага", "Математика", 9)
class_book_second = ClassBooks("Алгебра", "Иванов", 200, False, 464646, "бумага", "Математика", 9)
class_book_third = ClassBooks("Алгебра", "Иванов", 200, True, 454554, "бумага", "Математика", 9)


first_book.print_books()
second_book.print_books()
third_book.print_books()
fourth_book.print_books()
fives_book.print_books()
class_book_first.print_books()
class_book_second.print_books()
class_book_third.print_books()
