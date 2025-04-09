#class BMW
class BMW:
    def fuel_type(self):
       print("The fuel_type for BMW is diesel")
       
    def max_speed(self):
       print("The max_speed for BMW is 191mph")

#class ferrari
class ferrari:
    def fuel_type(self):
       print("The fuel_type for ferrari is premium fuel")
       
    def max_speed(self):
       print("The max_speed for ferrari is 211mph")
#object creation
obj_BMW = BMW()
obj_ferrari = ferrari()

#polymorphism
for car in (obj_BMW, obj_ferrari):
    car.fuel_type
    car.max_speed
        
#printing
print(obj_BMW.fuel_type)
print(obj_ferrari)