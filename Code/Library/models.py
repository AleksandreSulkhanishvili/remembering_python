class Librarian:
    def __init__(self, first_name, last_name, email, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.salary = salary
        self.books = []

    def __str__(self):
        return f"ბიბლიოთეკარი: {self.first_name} {self.last_name}, იმეილი: {self.email}, ასაკი {self.age}, შემოსავალი: {self.salary}"

    def add_book(self, book):
        self.books.append(book)


class User:
    def __init__(self, first_name, last_name, email, age, active_status=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.active_status = active_status
        self.checked_out_book = None

    def __str__(self):
        status = "აქტიური" if self.active_status else "პასიური"
        return f"მომხმარებელი: {self.first_name} {self.last_name}, მეილი: {self.email}, ასაკი {self.age}, სტატუსი: {status}"

    def check_out_book(self, book):
        if book.is_taken:
            print(f"წიგნი '{book.title}' უკვე გატანილია.")
            return False

        if self.checked_out_book is None:
            self.checked_out_book = book
            book.is_taken = True
            print(f"'{book.title}' უკვე გაიტანა {self.first_name}.")
            return True
        else:
            print(f"{self.first_name} უკვე აქვს წიგნი გატანილი.")
            return False

    def return_book(self):
        if self.checked_out_book is not None:
            self.checked_out_book.is_taken = False
            print(f"'{self.checked_out_book.title}' დააბრუნა {self.first_name}.")
            self.checked_out_book = None
        else:
            print(f"{self.first_name} დასაბრუნებელი წიგნი არ აქვს.")


class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Category: {self.name}"


class Book:
    def __init__(self, title, author, category, is_taken=False):
        self.title = title
        self.author = author
        self.category = category
        self.is_taken = is_taken

    def __str__(self):
        status = "გატანილი" if self.is_taken else "თავისუფალი"
        return f"წიგნი: '{self.title}' ავტორი: {self.author}, კატეგორია: {self.category.name} და სტატუსი: {status}"