class Books:
    have_text = True
    ISBN = 123456789123

    def __init__(self, name_book, author, pages, material, flag):
        self.name_book = name_book
        self.author = author
        self.pages = pages
        self.material = material
        self.flag = flag


first_book = Books("Идиот", "Достоевский", 500, "бумага", True)
second_book = Books("Идиот", "Достоевский", 500, "бумага", False)
third_book = Books("Идиот", "Достоевский", 500, "бумага", False)
fourth_book = Books("Идиот", "Достоевский", 500, "бумага", False)
fives_book = Books("Идиот", "Достоевский", 500, "бумага", False)


print(f'Название: {first_book.name_book}, Автор: {first_book.author}, страниц: {first_book.pages}, '
      f'материал: {first_book.material}, зарезервирована' if first_book.flag else
      f'Название: {first_book.name_book}, Автор: {first_book.author}, '
      f'страниц: {first_book.pages}, материал: {first_book.material}')
print(f'Название: {second_book.name_book}, Автор: {second_book.author}, страниц: {second_book.pages}, '
      f'материал: {second_book.material}, зарезервирована' if second_book.flag else
      f'Название: {second_book.name_book}, Автор: {second_book.author}, '
      f'страниц: {second_book.pages}, материал: {second_book.material}')
print(f'Название: {third_book.name_book}, Автор: {third_book.author}, страниц: {third_book.pages}, '
      f'материал: {third_book.material}, зарезервирована' if third_book.flag else
      f'Название: {third_book.name_book}, Автор: {third_book.author}, '
      f'страниц: {third_book.pages}, материал: {third_book.material}')
print(f'Название: {fourth_book.name_book}, Автор: {fourth_book.author}, страниц: {fourth_book.pages}, '
      f'материал: {fourth_book.material}, зарезервирована' if fourth_book.flag else
      f'Название: {fourth_book.name_book}, Автор: {fourth_book.author}, '
      f'страниц: {fourth_book.pages}, материал: {fourth_book.material}')
print(f'Название: {fives_book.name_book}, Автор: {fives_book.author}, страниц: {fives_book.pages}, '
      f'материал: {fives_book.material}, зарезервирована' if fives_book.flag else
      f'Название: {fives_book.name_book}, Автор: {fives_book.author}, '
      f'страниц: {fives_book.pages}, материал: {fives_book.material}')


class ClassBooks(Books):
    tasks = True

    def __init__(self, name_book, author, pages, flag, material, subject, school_class):
        super().__init__(name_book, author, pages, material, flag)
        self.subject = subject
        self.school_class = school_class


class_book_first = ClassBooks("Алгебра", "Иванов", 200, False, "бумага",  "Математика", 9)
class_book_second = ClassBooks("Алгебра", "Иванов", 200, False, "бумага", "Математика", 9)
class_book_third = ClassBooks("Алгебра", "Иванов", 200, True, "бумага", "Математика", 9)


print(f'Название: {class_book_first.name_book}, Автор: {class_book_first.author}, страниц: {class_book_first.pages}, '
      f'предмет: {class_book_first.subject}, '
      f'класс: {class_book_first.school_class}, зарезервирована' if class_book_first.flag else
      f'Название: {class_book_first.name_book}, Автор: {class_book_first.author}, '
      f'страниц: {class_book_first.pages}, предмет: {class_book_first.subject}, '
      f'класс: {class_book_first.school_class}')
print(f'Название: {class_book_second.name_book}, Автор: {class_book_second.author}, страниц: {class_book_second.pages},'
      f'предмет: {class_book_second.subject}, '
      f'класс: {class_book_second.school_class}, зарезервирована' if class_book_second.flag else
      f'Название: {class_book_second.name_book}, Автор: {class_book_second.author}, '
      f'страниц: {class_book_second.pages}, предмет: {class_book_second.subject}, '
      f'класс: {class_book_second.school_class}')
print(f'Название: {class_book_third.name_book}, Автор: {class_book_third.author}, страниц: {class_book_third.pages}, '
      f'предмет: {class_book_third.subject}, '
      f'класс: {class_book_third.school_class}, зарезервирована' if class_book_third.flag else
      f'Название: {class_book_third.name_book}, Автор: {class_book_third.author}, '
      f'страниц: {class_book_third.pages}, предмет: {class_book_third.subject}, '
      f'класс: {class_book_third.school_class}')
