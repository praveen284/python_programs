class Vehicle:
	color="White"
	def __init__(self,name,speed,milage,seating_capacity):
		self.name=name
		self.speed=speed
		self.milage=milage
		self.seating_capacity=seating_capacity

class Bus(Vehicle):
	def __init__(self,name,speed,milage,seating_capacity,fare_charge):
		super().__init__(name,speed,milage,seating_capacity)
		self.fare_charge=fare_charge
		

	def fare(self):
		return (self.fare_charge*self.seating_capacity)+(0.1*self.fare_charge*self.seating_capacity)
		

class Car(Vehicle):
	pass

print("<<<.........Bus...........>>>")	
b=Bus("School Volvo",180,12,50,100)
print("Color:",b.color,"Name:",b.name,"max_speed:",b.speed,"Seating_capacity:",b.seating_capacity,"Fare:",b.fare())

print("\n")

# print("<<<........Car............>>>")
# c= Car("Audi Q5", 240, 20, 18)
# print("Color:",c.color,"Name:",c.name,"max_speed:",c.speed,"Seating_capacity:",c.seating_capacity)