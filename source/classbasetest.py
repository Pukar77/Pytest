class shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class circle(shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius *self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
    
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length+self.width) 
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        
       
if __name__ == '__main__':
    s=Square(5)
    print(s.area())