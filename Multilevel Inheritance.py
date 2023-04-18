class Vehicle:
    def vehicle(self):
        print("A vehicle is a machine that transport people or cargo.")

class Car(Vehicle):
    def car(self):
        print("A car is it gives the freedom to travel.")

class BMW(Car):
    def bmw(self):
        print("BMW is performance  and luxury models")

ob = BMW()
ob.vehicle()
ob.car()
ob.bmw()
