class electric_Bike:
    
    wheels = 2  # Class attribute shared by all electric_Bike instances
    num_total = 0  # Class attribute to count total number of electric bikes
    def __init__(self, brand, type_of_bike):
        self.brand = brand
        self.type_of_bike = type_of_bike
        electric_Bike.num_total += 1  # Increment wheels for each new bike instance

    @classmethod 
    def total_electric_bike(tls):
        print(f"{electric_Bike.num_total}")

    def Type_of_Electric_Bike(self):
        print(f"The type of the electric bike is a {self.type_of_bike} with the wheels of {electric_Bike.wheels}.")
        
Ebike1 = electric_Bike("Giant", "Mountain Bike")
Ebike2 = electric_Bike("Trek", "Road Bike")
Ebike3 = electric_Bike("Specialized", "Hybrid Bike")
Ebike4 = electric_Bike("Cannondale", "Folding Bike")

print(f"total of electric bikes: {electric_Bike.num_total}")

Ebike1.Type_of_Electric_Bike()
Ebike2.Type_of_Electric_Bike()
