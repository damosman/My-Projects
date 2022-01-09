# Write a python program
# The program should be able to display the features of different brands of cars
# Create a Vehicle class with below attributes:
    # Color (5 colors)
    # Transmission (Auto, Manual)
    # Brand (Toyota, BMW, VW, Nissan, Volvo)
    # Model (create 3 models of each brand)
    # Fuel_Type (95, Diesel, Gas, Electricity)

# Define 5 unique methods/functions that the Vehicle should be able to perform

# Create 5 objects of the class vehicle to display a list of all the features and functionalities of each of the objects


color = ['blue', 'red', 'yellow', 'black', 'white']
trans = ['Automatic', 'Manual']
brand = ['Toyota', 'BMW', 'VW', 'Nissan', 'Volvo']
model = ['Avalon', 'Camry', 'Supra', 'X3', 'X5', 'i8']
fuel_type = ['95', 'Diesel', 'Gas', 'Electricity']
class Vehicle:
  def __init__(self, color, trans,brand,model, fuel_type):
    self.color = color
    self.trans = trans
    self.brand = brand
    self.model = model
    self.fuel_type = fuel_type

  def drive(self):
    print(f"I drive a", self.color, self.brand, self.model, "car with", self.trans, "and runs on", self.fuel_type)

_car = Vehicle(brand= brand[0], color= color[0], model= model[1], trans=trans[0], fuel_type=fuel_type[3] )
_car.drive()


