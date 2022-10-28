import geometry_tools as gt
import convex_hull
from segments_intersect import any_segments_intersect

def convex_segments(P):
    '''
    Retorna os segmentos que formam
    a envoltoria convexa
    '''
    H = gt.make_points(P)

    segments_points = []
    segments = []
    #hull = convex_hull.graham_scan(H)
    hull = convex_hull.gift_wrap(H)
    for i in hull:
        segments_points.append(gt.Point(i.x, i.y,))
    
    n = len(segments_points)
    for i in range(n):
        segments.append(gt.Point(segments_points[i].x, segments_points[i].y, p_type=0, other_end=segments_points[(i+1)%n]))
        #segments.append(gt.Point(segments_points[i].x, segments_points[i].y, p_type=0, other_end=segments_points[(i-1)%n]))
    
    return segments

def separability(H1, H2):
    '''
    Verifica se duas envoltorias H1 e H2
    se interceptam
    '''

    H = H2 + H1
    return any_segments_intersect(H)

def shortest_points(H1, H2):
    points = [0,1]
    if not(separability(H1, H2)):
        min_dist = 9999999999
        for i in H1:
            for j in H2:
                if gt.distance(i, j) < min_dist:
                    min_dist = gt.distance(i, j)
                    points[0] = i
                    points[1] = j
        return points
    return False

def line_eq(p1, p2):
    m = (p2.y - p1.y) / (p2.x - p1.x)
