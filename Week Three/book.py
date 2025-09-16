class Book:
    def __init__(self, name, author, publisher, genre, year_published):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.year_published = year_published


Book1 = Book("Beloved", "Toni Morrison", "Alfred A. Knopf", "Magical Realism", "1987")
Book2 = Book("Frankenstein", "Mary Shelley", "Lackington", "Science Fiction", "1818")
Book3 = Book(
    "Dracula", "Bram Stoker", "Archibald Constable and Company", "Gothic Horror", "1897"
)

print(Book1.name)
print(Book2.author)
print(Book3.year_published)
