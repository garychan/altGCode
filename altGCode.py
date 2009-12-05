import sys


ALT_START = """
M106
"""

ALT_STOP = """
M107
M126
"""

START_CODE = """
(start code)
M106
G4 P100 
(end of start code)
"""

STOP_CODE = """
(stop code)
M107
M126
G4 P100
M127 
(end of stop code)
"""

WARMUP_SEQUENCE = """
(warmup sequence)
G21
G90
G92 X0 Y0 Z0
G00 Z0 F1100.00 
(end of warmup)
"""

COOLDOWN_SEQUENCE = """
(cool down)
M107
M126
G4 P100
M127
G00 Z10 F200 
(end of cool down sequence)
"""


class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    
class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
class Grid:

    def __init__(self, width, height, resolution): 
        self.width = width
        self.height = height
        self.resolution = resolution
        
        self.horizontalPoints = self.max_points(width, resolution)
        self.verticalPoints = self.max_points(height, resolution)
        
        self.genCode = []
         
        
    def max_points(self, w, r):
        if r < 10:
            return (w / r) - 1
        return w / r
        
    def append(self, o):
        self.genCode.append("G01 X%s Y%s F5 (point -> speed 5 per inch)" % (o.x, o.y))
        self.genCode.append("G04 P2 (Pause for 2s)")
        self.genCode.append(ALT_START)
        self.genCode.append(ALT_STOP)
    
    def generate(self):
        sys.stdout.writelines(WARMUP_SEQUENCE)
        sys.stdout.writelines(START_CODE)
        sys.stdout.writelines("G00 X%s Y%s (go to top left corner -> making axis positive)\n" % ((-self.width/2), (-self.height/2)))
        for line in self.genCode:
            sys.stdout.write(line + "\n")
        sys.stdout.writelines(STOP_CODE)
        sys.stdout.writelines(COOLDOWN_SEQUENCE)
        
        
