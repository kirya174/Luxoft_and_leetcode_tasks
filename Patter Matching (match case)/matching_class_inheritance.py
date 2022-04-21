class Point:
    __match_args__ = ('x', 'y')
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle(Point):
    __match_args__ = ('x','y','x1','y1')
    def __init__(self,x,y,x1,y1):
        super().__init__(x,y)
        self.x1 = x1
        self.y1 = y1
        
shape = Rectangle(1,2,3,4)

# go to Point
match shape:
    case Point(x,y):
        print(f"Point with coord {x},{y}")
    case Rectangle(x0,y0,x1,y1):
        print(f"Rectang with coord {x0},{y0} and {x1},{y1}")
    case _:
        print("unknown object")

# go to Rectangle       
match shape:
    case Rectangle(x0,y0,x1,y1):
        print(f"Rectang with coord {x0},{y0} and {x1},{y1}")
    case Point(x,y):
        print(f"Point with coord {x},{y}")    
    case _:
        print("unknown object")