class WaterDispenser:
    def __init__(self, brand, has_cooler, has_heater):
        self.brand = brand
        self.has_cooler = has_cooler
        self.has_heater = has_heater

    def dispense_cold_water(self):
        print(f"Dispensing cold water from {self.brand} with {self.has_cooler} degree water.")
    def dispense_hot_water(self):
        print(f"Dispensing hot water from {self.brand} with {self.has_heater} degree water.")