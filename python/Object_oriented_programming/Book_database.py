class TooMuchwidth(Exception): pass


class Book:
    def __init__(self, title, author, price, width) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf:
    def __init__(self, width) -> None:
        self.books = []
        self.width = width

    def add_books(self, *new_book):
        if sum(wb.width for wb in new_book) <= self.width:
            for book in new_book:
                self.books.append(book)
        else:
            raise TooMuchwidth ("Too much for the shelf")
    
    def total_price(self):
        total_price = sum(b.price for b in self.books)
        return total_price

    def has_book(self, title_checker):
        if title_checker in [title.title for title in self.books]:
            return True
        return False

book1 = Book("OOP", "Ahmed", 23400, 22)
book2 = Book("Python Workout", "Reuven", 9000, 12)
shelf1 = Shelf(35)
shelf1.add_books(book1, book2)
print(shelf1.total_price())
shelf1.has_book(";la")
