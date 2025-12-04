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
    def __init__(self, name, vehicle, driver, item):
        super().__init__(name)
        self.name = name
        self.vehicle = vehicle
        self.driver = driver
        self.item = item
    
    def deliver(self,order):
        print(f"{self.driver} is delivering {self.item} to {self.name} using {self.vehicle}.")
        self.order = order

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
        print("")
    
    def final(self,status = "delivered"):
        self.status = status
        # print("")
        #print("Final Status:")
        print(f"Order for {self.item} → {self.status}")

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
dri1 = Driver("Alice","motorcycle","David","Laptop")
dri1.deliver("Headphones")
dri2 = Driver("Bob","motorcycle","David","Headphones")
dri2.deliver("Headphones")
print("")

print("Final Status:")
fi1 = DeliveryOrder("Alice","Laptop","David")
fi1.final()
fi2 = DeliveryOrder("Bob","Headphones","David")
fi2.final()