class Shoe():
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        
    def wear(self):
        print (f"Wear the {self.brand} {self.color} with a size {self.size}.")

    def remove(self):
        print (f"Remove the {self.brand} {self.color} with a size {self.size}.")