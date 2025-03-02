class vehicle:
    def __init__ (self, name, maximum_speed, mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage

class bus(vehicle):
    pass

b1 = bus("school volvo", 200, 10 )
print("The name of the bus is" ,b1.name)
print("The maximum speed of the bus is" ,b1.maximum_speed)
print("The mileage of the bus is" ,b1.mileage)