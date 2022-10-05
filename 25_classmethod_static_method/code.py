class ClassTest:
    def instance_method(self):
        print(f"Called the instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called the class_method of {cls}")

    @classmethod
    def new(cls):
        print(f"Called the class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method.")


test = ClassTest()
test.instance_method()

ClassTest.class_method()
ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, {self.weight}>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book("Harry Potter", "hardcover", 1500)
print(book.name)

print(Book.TYPES)

book = Book.hardcover("Harry Potter", 1200)
print(book)