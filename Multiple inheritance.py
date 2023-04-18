class Desktop:
    def desk(self):
        print("Desktop can add more storage , RAM, and a better graphics.")

class Laptop:
    def lap(self):
        print("Laptops are the best used for light work.")

class Dell(Desktop, Laptop):
    def dell(self):
        print("Dell is one of the world's largest PC.")

ob = Dell()
ob.desk()
ob.lap()
ob.dell()
