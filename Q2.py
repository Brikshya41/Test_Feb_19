'''Create a class circle which has a class variable PI with tha value==22/7. Make two methods getArea and getCircumference inside this Circle class.
 Which when invoked returns area and circumference of each circle instances.'''


class Circle:
    PI=22/7
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return Circle.PI*self.radius**2

    def getCircumference(self):
        return 2*Circle.PI*self.radius


s= Circle(5)
print(s.getArea())
print(s.getCircumference())
