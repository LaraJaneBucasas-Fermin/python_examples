class Book():
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
    def open(self):
        print (f"Open the {self.title} by {self.author} with  the genre {self.genre}.")

    def read(self):
        print (f"Read the {self.title} {self.author} with the genre {self.genre}.")