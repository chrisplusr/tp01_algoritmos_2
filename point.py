class Point:
    def __init__(self, x, y, p_type=0, other_end=None):
        self.x = x
        self.y = y
        self.p_type = p_type
        self.other_end = other_end
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __eq__(self, p):
        return True if (self.x == p.x and self.y == p.y) else False

    def __ne__(self, p):
        return True if (self.x != p.x and self.y != p.y) else False

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __bool__(self):
    	return True
    
    def __nonzero__(self):
    	return True
