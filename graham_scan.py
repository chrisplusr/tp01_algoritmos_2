from functools import cmp_to_key
import merge_sort as ms
import point

def min_point(P):
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
    r1 = Pk - Pi
    r2 = Pj - Pi
    return (r1.x * r2.y) - (r1.y * r2.x)

def dist(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) +
            (p1.y - p2.y) * (p1.y - p2.y))

def cmp(p1, p2, p0):
    d = direction(p0, p1, p2)
    if d < 0:
        return -1
    if d > 0:
        return 1
    if d == 0:
        if dist(p1, p0) < dist(p2, p0):
            return -1
        else:
            return 1

def remove_duplicates(P, p0):
    n = len(P)
    m = 0
    remove = []
    for i in range(n-1):
        while(i < n-1 and direction(p0, P[i], P[i+1]) == 0):
            i += 1
        if(P[m] != P[i]):
            if(P[m].x > P[i].x):
                remove.append(P[i])
            else:
                remove.append(P[m])
        m += 1
    for i in remove:
        P.remove(i)

def graham_scan(P):
    p0 = min_point(P)

    P_s = sorted(P, key=cmp_to_key(lambda x,y: cmp(x,y,p0)))
    remove_duplicates(P_s,p0)
    
    s = []
    s.append(p0)
    s.append(P_s[0])
    s.append(P_s[1])
    size = 3
    for i in range(2, len(P_s)):
        while direction(P_s[i], s[size-2], s[size-1]) > 0:
            s.pop()
            size -= 1
        s.append(P_s[i])
        size += 1
    return s
        
'''
# Teste
P1 = [(0, 6), (4, 9), (3, 10), (6, 7), (9, 7), (10, 8), (16, 7), (20, 6), (19, 3), (3, 11), (22, 6), (20, 4), (8, 0)]
P = [(-4.2495924153363,0.0116196743617),
(-2.4918882285364,0.2838083668922),
(-2.7324151760349,1.7871017887581),
(-4.6365868437316,2.2080239468805),
(-5.5385628968511,1.9875409116735),
(-4.5564111945655,0.604510963557),
(-3.9350499135276,1.1456965954287),
(-4.8570698789386,1.3461357183441),
(-5.1176407387287,1.6868822273003),
(-4.4962794576908,1.8672774379242)]
points = []

for i in P:
    points.append(point.Point(i[0], i[1]))
graham_scan(points)
'''
