# OOP - Class - inheritance

#base class
class Car:
    def __init__(self):
        self.height =12
    
    def drive(self):
        print("Driving the car....")

#sub class
class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.engine = "400"
        
    def drive(self): ## method overriding
        print("Driving the car for sportsCar....")
# object for subclass
SportsCar = SportsCar()
SportsCar.drive()
print(SportsCar.height)  # from Car
print(SportsCar.engine)  # from SportsCar


