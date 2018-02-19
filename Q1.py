class RectangleGeometry:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def getArea(self):
        return self.length*self.breadth

    def getPerimeter(self):
        return 2*self.length+2*self.breadth


s=rectangleGeometry(5)
print(s.getArea())
print(s.getPerimeter())
