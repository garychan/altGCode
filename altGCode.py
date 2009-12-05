import sys


ALT_START = "M106"

ALT_STOP = """M107
M126"""

START_CODE = """
(start code)
M106 (open left valve)
G4 P100 (pause .1s)
(end of start code)
"""

STOP_CODE = """
(stop code)
M107 (close left valve)
M126 (open right valve)
G4 P100 (pause .1s)
M127 (close right valve)
(end of stop code)
"""

WARMUP_SEQUENCE = """
(warmup sequence)
G21 (Programming in mm)
G90 (Absolute programing)
G92 X0 Y0 Z0 (set 0 point)
G00 Z0 F1100.00 (Feed rate) 
(end of warmup)
"""

COOLDOWN_SEQUENCE = """
(cool down)
M107 (close left valve)
M126 (open right valve)
G4 P100 (pause .1s)
M127 (close right valve)
G00 Z10 F200
(end of cool down sequence)
"""


class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
        
    def gcode(self, resolution):
        genCode = []
        genCode.append("G01 X%s Y%s (move to point)" 
            % (self.x * resolution, self.y * resolution))
        genCode.append(ALT_START)
        genCode.append("G04 P2000 (Pause for 2s)")
        genCode.append(ALT_STOP)
        
        return "\n".join(genCode)
    
class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def gcode(self, resolution):
        return None
      

class Circle:
    """this function is not yet finished"""
    def __init__(self, centerPoint, radius):
        self.centerPoint = centerPoint
        self.radius = raidus
    def gcode(self, resolution):
        genCode = []
        genCode.append("G01 X%s Y%s (move to first circle point)"
                       %(self.centerPoint.x - radius, self.centerPoint.y))

                      
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
        self.genCode.append(o)
    
    def generate(self):
        sys.stdout.writelines(WARMUP_SEQUENCE)
        sys.stdout.writelines(START_CODE)
        for line in self.genCode:
            sys.stdout.write(line.gcode(self.resolution) + "\n")
        sys.stdout.writelines(STOP_CODE)
        sys.stdout.writelines(COOLDOWN_SEQUENCE)
        
        
