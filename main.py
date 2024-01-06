class Book:
    def __init__(self, title, author, description, genre):
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

#Добавляет книгу в библиотеку.
    def add_book(self, book):
        self.books.append(book)

#Удаляет книгу из библиотеки по названию.
    def remove_book(self, title):
        for book in self.books[:]:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{title}' удалена из библиотеки.")
                return
        print(f"Книга с названием '{title}' не найдена в библиотеке.")

#Поиск книги по ключевому слову в названии, авторе или жанре.
    def search_books(self, keyword):
        result_books = [book for book in self.books if keyword.lower() in (book.title + book.author + book.genre).lower()]
        return result_books

#Выводит список книг в библиотеке.
    def display_books(self, books_to_display=None):
        books_to_display = books_to_display or self.books
        print("Список книг в библиотеке:")
        for book in books_to_display:
            print(f"{book.title} - {book.author}")

#Выводит подробную информацию о книге.
    def display_book_details(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Информация о книге '{book.title}':")
                print(f"Автор: {book.author}")
                print(f"Жанр: {book.genre}")
                print(f"Описание: {book.description}")
                return
        print(f"Книга с названием '{title}' не найдена в библиотеке.")

#Выводит список книг по указанному жанру.
    def display_books_genre(self, genre):
        genre_books = [book for book in self.books if book.genre.lower() == genre.lower()]
        if genre_books:
            print(f"Список книг по жанру '{genre}':")
            for book in genre_books:
                print(f"{book.title} - {book.author}")
        else:
            print(f"Нет книг в жанре '{genre}' в библиотеке.")

# Создание экземпляра класса Library.

library = Library()

# Добавление книг.
book1 = Book("Книга 1", "Автор 3", "Описание 1", "Роман")
book2 = Book("Книга 2", "Автор 2", "Описание 2", "Драма")
book3 = Book("Книга 3", "Автор 1", "Описание 3", "Комедия")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Просмотр списка книг.
library.display_books()

# Просмотр подробной информации о книге.
book_title = "Книга 1"
library.display_book_details(book_title)

# Вывод книг по жанру.
genre_to_display = "Драма"
library.display_books_genre(genre_to_display)

# Поиск книги.
search_keyword = "автор 2"
result_books = library.search_books(search_keyword)
print(f"Результаты поиска по ключевому слову '{search_keyword}':")
library.display_books(result_books)

# Удаление книги.
book_to_remove = "Книга 2"
library.remove_book(book_to_remove)
library.display_books()
