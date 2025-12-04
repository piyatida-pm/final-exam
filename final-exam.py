class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, adress):
        super().__init__(name)
        self.adress = adress
    
    def place_order(self,item):
        self.item = item
        return 
    
class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.name = name
        self.vehicle = vehicle
    
    def deliver(self,order):
        print(f"{self.name}  is delivering to {self.name} using {self.vehicle}")
        order = "delivered"

class DeliveryOrder:
    def __init__(self,customer,item,driver,status= "preparing"):
        self.customer = customer
        self.item = item
        self.status = status
        self.driver = driver
    
    def assign_driver(self,driver):
        self.driver = driver

    def summary(self):
        print("\nOrder Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.driver}")

cos1 = Person("Alice")
cos2 = Person("Bob")     
cos1.introduce()
cos2.introduce()
deli1 = Person("David")
deli1.introduce()
ordersum = DeliveryOrder("Alice","Laptop","David")
ordersum.summary()
ordersum = DeliveryOrder("Bob","Headphones","David")
ordersum.summary()
dri1 = Driver("Alice","motorcycle")
dri1.deliver("Headphones")