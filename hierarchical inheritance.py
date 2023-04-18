class Vehicle:
    def vehicle(self):
        print("A vehicle is a machine that transport people or cargo")

class Car(Vehicle):
    def car(self):
        print("A car is it gives the freedom to travel.")

class Train(Vehicle):
    def train(self):
        print("Travelling by train can be convenient")

ob = Car()
ob1 = Train()
ob.vehicle()
ob.car()
ob1.vehicle()
ob1.train()
