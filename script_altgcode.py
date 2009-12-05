from altGCode import *

g = Grid(90, 90, 10)

for y in xrange(0, g.verticalPoints+1):    
    for x in xrange(0, g.horizontalPoints+1):
        g.append(Point(x, y))
        
g.generate()
