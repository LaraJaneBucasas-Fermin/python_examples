from Book import Book
from Shoe import Shoe
from Cup import Cup

book1 = Book("1984", "George Orwell", "Mystery")
cup1 = Cup("Coffee", "Medium", "Red")
shoe1 = Shoe("Nike", 42, "Black")

print(book1.title, book1.author, book1.genre)

cup1.drink()
cup1.fill()
book1.open()
book1.read()
shoe1.remove()
shoe1.wear()