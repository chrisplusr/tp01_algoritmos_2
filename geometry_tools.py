import math

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


def min_point(P):
    '''
    Função que retorna o ponto com a menor coodernada y
    se houver empate retorna o ponto com a menor coodernada x
    '''
    p_min = P[0]
    
    for i in range(1, len(P)):
        if P[i].y <= p_min.y:
            if P[i].y == p_min.y:
                if P[i].x < p_min.x:
                    p_min = P[i]
            else:
                p_min = P[i]
    
    P.remove(p_min)
    return p_min

def direction(Pi, Pj, Pk):
    '''
    Retorna o produto cruzado entre os segmentos
    Pj-Pi e Pk-Pi consequentemente a direçao da reta
    Pj-Pi em relaçao a Pk-Pi
    '''
    r1 = Pk - Pi
    r2 = Pj - Pi
    return (r1.x * r2.y) - (r1.y * r2.x)

def distance(p1, p2):
    '''
    Retorna a distancia entre dois pontos
    '''
    return math.sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))

def on_segment(Pi, Pj, Pk):
    '''
    Retorna se o ponto Pk esta na reta Pj-Pi
    mas Pk não é os pontos extremos
    '''
    if(min(Pi.x, Pj.x) < Pk.x and Pk.x < max(Pi.x, Pj.x)) and (min(Pi.y, Pj.y) < Pk.y and Pk.y < max(Pi.y, Pj.y)):
        return True
    else:
        return False

def intersect(p1, p2, p3, p4):
    '''
    Retorna true se os segmentos se interseptam
    '''
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    if((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True    
    else:
        return False

def make_points(P):
    '''
    Cria os pontos a partir da lista de tuplas
    '''
    H = []
    for i in P:
        H.append(Point(i[0], i[1]))
    return H

