class Triangle:
    def __init__(self,size:int,pattern:str,direction:str):
        self.size = size
        self.pattern = pattern
        self.direction = direction

    def display(self):
        if pattern == "l":
            for i in range(0,size):
                print(pattern * (i+1))
        elif pattern == "r":


        #d = Triangle(self.display())

size = int(input("Enter triangle size: "))
pattern = input("Enter pattern: ")
direct = input("Enter direction (L/R): ").lower()
tri = Triangle(size,pattern,direct)
