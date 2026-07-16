class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)
        print(f'"{title}" added.')

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(f'"{title}" removed.')
        else:
            print("Book not found.")

    def list_books(self):
        if not self.__books:
            print("Library is empty.")
        else:
            print("Books in Library:")
            for book in self.__books:
                print("-", book)


library = Library()

library.add_book("Atomic Habits")
library.add_book("Rich Dad Poor Dad")
library.add_book("Python Programming")

library.list_books()

library.remove_book("Rich Dad Poor Dad")

library.list_books()