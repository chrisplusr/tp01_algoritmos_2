import geometry_tools as gt
import convex_hull
import segments_intersect as si

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
        #segments.append(gt.Point(segments_points[i].x, segments_points[i].y, p_type=1, other_end=segments_points[(i-1)%n]))
    
    return segments

def separability(H1, H2):
    '''
    Verifica se duas envoltorias H1 e H2
    se interceptam
    '''
    
    #return si.any_segments_intersect(H1, H2)
    
    return si.naive_alg(H1, H2)

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

def class_model(H1, H2):
    points = shortest_points(H1, H2)
    class1 = []
    class2 = []

    if points != False:
        pm = gt.Point(((points[0].x + points[1].x)/2), ((points[0].y + points[1].y)/2))
        val = min(max(H1, key=lambda p: p.x).x, max(H1, key=lambda p:p.y).y)
        line = [gt.Point(pm.x - val, pm.y + val), gt.Point(pm.x + val, pm.y - val)]
        
        for i in H1:
            d = gt.direction(line[0], i, line[1])

            if d > 0:
                class1.append(i)
            else:
                class2.append(i)

        for i in H2:
            d = gt.direction(line[0], i, line[1])

            if d > 0:
                class1.append(i)
            else:
                class2.append(i)
        return class1, class2
    
    
