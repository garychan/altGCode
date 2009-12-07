from altGCode import *

g = Grid(90, 90, 10)
g.append(Circle(Point(45, 45), 20, 20))
g.generate()


def circle(radius): 
    x = 0 
    y = radius 
    switch = 3 - (2 * radius) 
    points = [] 
    while x <= y: 
        points.extend([(x,y),(x,-y),(-x,y),(-x,-y),\
            (y,x),(y,-x),(-y,x),(-y,-x)]) 
        if switch < 0: 
            switch = switch + (4 * x) + 6 
        else: 
            switch = switch + (4 * (x - y)) + 10 
            y = y - 1 
            x = x + 1 
    return points 
