class animalGenerator:
    animal_total = 0 
    def __init__(self,type,breed,labName,color,superpower,strength,weakness):
        self.type = type
        self.breed = breed
        self.labName = labName
        self.color = color
        self.superpower = superpower
        self.strength = strength
        self.weakness = weakness
        animalGenerator.animal_total += 1  
        
    @classmethod
    def total_animals(tls):
        print(f"{animalGenerator.animal_total}")
        
    def animal_details(self):
        print(f"The animal is a {self.type}: {self.breed}, named {self.labName}, color: {self.color}, superpower: {self.superpower}.")
        
    def animal_strength(self):
        print(f"The strength of the {self.labName}: {self.strength}.")
        
    def animal_weakness(self):
        print(f"The weakness of the {self.labName}: {self.weakness}.")