class Point:
    __match_args__ = ('x','y')
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Rectangle:
    __match_args__ = ('x0','y0','x1','y1','painted')
    def __init__(self,x0,y0,x1,y1,painted):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.painted = painted
        
        
#shape = Point(1,2)
#shape = Rectangle(1,2,3,4,False)
shape = Rectangle(1,2,3,4,True)

match shape:
    case Point(x,y):
        print(f"Point with coord {x} and {y}")
    case Rectangle(x0,y0,x1,y1,painted = True):
        print(f"Rectang with coord {x0},{y0} and {x1},{y1}")
    case _:
        print("unknown object")
        
    

    