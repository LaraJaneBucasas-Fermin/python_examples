class Cup():
    def __init__(self, type_drinks, size, color):
        self.type_drinks = type_drinks
        self.size = size
        self.color = color
        
    def fill(self):
        print (f"Filling the {self.size} {self.color} cup with {self.type_drinks}.")

    def drink(self):
        print (f"Drinking the {self.size} {self.color} cup with {self.type_drinks}.")