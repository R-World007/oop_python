class Vehicle:
    def vehicle(self):
        print("A vehicle is a machine that transport people or cargo")

class Car(Vehicle):
    def car(self):
        print("A car is it gives the freedom to travel.")

class Train(Vehicle):
    def train(self):
        print("Travelling by train can be convenient")

class BMW(Car,Vehicle):
    def bmw(self):
        print("BMW is performance  and luxury models")

ob = BMW()
ob1 = Train()
ob1.train()
ob.vehicle()
ob.car()
ob.bmw()

