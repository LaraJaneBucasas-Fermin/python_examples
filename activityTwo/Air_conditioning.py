class Air_conditioning:
    def __init__(self, brand, model, temperature):
        self.brand = brand
        self.model = model
        self.temperature = temperature

    def set_temperature(self):
        print(f"Set the temperature of {self.brand} to {self.temperature} degrees")

    def turn_on(self):
        print(f"Turn on the {self.brand} {self.model} air conditioner.")
