class Oven:
    def __init__(self, brand, capacity, item):
        self.brand = brand
        self.capacity = capacity
        self.item = item

    def bake(self):
        print (f"Baking {self.item} in the {self.brand} with the capacity of {self.capacity} oven.")
    def clean(self):
        print (f"Clean the {self.brand} with the capacity of {self.capacity}.")        