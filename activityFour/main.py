from animalGenerator import animalGenerator


animal1 = animalGenerator("Dog", "Labrador", "Superdog", "Yellow", "Super Strength", "High endurance", "Kryptonite")
animal2 = animalGenerator("Cat", "Siamese", "Whiskers", "Cream", "Invisibility", "Agility", "Water")
animal3 = animalGenerator("Bird", "Parrot", "Hipo", "Green", "Hypnosis", "Mimicry", "Loud Noises")

animal1.animal_details()
animal1.animal_strength()
animal1.animal_weakness()
animal2.animal_details()
animal2.animal_strength()
animal2.animal_weakness()    
animal3.animal_details()
animal3.animal_strength()
animal3.animal_weakness()
print(f"Total of Animals: {animalGenerator.animal_total}")