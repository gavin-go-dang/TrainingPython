
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    count = 0

    def __init__(self, name):
        self.__name = name
        self.__n = 0
        Shape.count += 1

    @abstractmethod
    def area(self):
        print('Dien tich cua hinh')

    @abstractmethod
    def circum(self):
        print('Chu vi cua hinh')


    @classmethod
    def num_of_shape(cls):
        return cls.count
    
    def get_name(self):
        return self.__name


class Triangle(Shape):

    count = 0
    list_shape = list()

    def __init__(self, name, *agrv):        
        super().__init__(name)
        if name not in Triangle.list_shape:
            
            self.__n = 3
            if agrv:
                self.parametter = list(agrv)

            Triangle.count += 1
            Triangle.list_shape.append(name)

    @property
    def area(self):
        p = (self.parametter[0] + self.parametter[1] + self.parametter[2]) / 2
        S = math.sqrt(p * (p - self.parametter[0]) * (p - self.parametter[1]) * (p - self.parametter[2]))
        return S
    
    @property 
    def circum(self):
        return self.parametter[0] + self.parametter[1] + self.parametter[2]
    


class Retangle(Shape):
    count = 0
    list_of_shape = list()

    def __init__(self, name, *agrv):
        super().__init__(name)
        if  name not in Retangle.list_of_shape:            
            self.__n = 4
            if agrv:
                self.parametter = list(agrv)
            Retangle.count += 1
            Retangle.list_of_shape.append(name)

    @property
    def area(self):
        return self.parametter[0] * self.parametter[1]
    

    @property
    def circum(self):
        return 2 *(self.parametter[0] + self.parametter[1])


class Square(Shape):
    count = 0
    list_of_shape = list()

    def __init__(self, name, *agrv):
        super().__init__(name)
        if  name not in Square.list_of_shape:
            
            self.__n = 4
            if agrv:
                self.parametter = list(agrv)
            Square.count += 1
            Square.list_of_shape.append(name)

    @property
    def area(self):
        return self.parametter[0] * self.parametter[0]
    
    @property
    def circum(self):
        return self.parametter[0] * 4


class Circle(Shape):
    count = 0
    list_of_shape = list()

    def __init__(self, name, *agrv):
        super().__init__(name)
        if  name not in Circle.list_of_shape:
            
            self.__n = 0
            if agrv:
                self.parametter = list(agrv)
            Circle.count += 1
            Circle.list_of_shape.append(name)

    @property
    def area(self):
        return self.parametter[0] * self.parametter[0] * 3.14
    
    @property
    def circum(self):
        return self.parametter[0] * 2 * 3.14