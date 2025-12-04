import math

class Object3D:
    def __init__(self, label: str, object_type: str, dimension: float) -> None:
        self.__label = label.lower()
        self.__object_type = object_type.lower()
        self.__dimention = dimension

    def __volume__(self) -> float:
        self.cube = (self.__dimention ** 3)
        self.sphere = ((4/3)*math.pi) * (self.__dimention ** 3)
        self.pyramid = 1/3 * (self.__dimention ** 3)

    def get_info(self):
        return f"Label: {self.__label}, Object: {self.__label}, Dimension: {self.__dimention}, Volume: {self.__volume__}"
    
while True:
    label = input("Enter label (or EXIT to stop): ")
    if label == "EXIT":
        print("-----REPORT-----")
        print("No object recorded")
        break
    type = input("Enter object type (cube, sphere, pyramid): ")
    dimen = float(input("Enter dimension: "))
    



        