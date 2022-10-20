from functools import cmp_to_key
import red_black_tree as rbt
import point

def on_segment(Pi, Pj, Pk):
    if(min(Pi.x, Pj.x) <= Pk.x and Pk.x <= max(Pi.x, Pj.x)) and (min(Pi.y, Pj.y) <= Pk.y and Pk.y <= max(Pi.y, Pj.y)):
        return True
    else:
        return False

def intersect(p1, p2, p3, p4):
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

def direction(Pi, Pj, Pk):
    r1 = Pj - Pi
    r2 = Pk - Pi
    return (r1.x * r2.y) - (r1.y * r2.x)

def cmp_points(p1, p2):
    if p1.x < p2.x:
        return -1
    elif p1.x > p2.x:
        return 1
    if p1.x == p2.x:
        if p1.p_type == p2.p_type:
            if p1.y < p2.y:
                return -1
            else:
                return 1
        else:
            if p1.p_type == 0:
                return -1
            else:
                return 1

def any_segments_intersect(S):
    T = rbt.RedBlackTree()

    sorted_segments = sorted(S, key=cmp_to_key(cmp_points))
    sorted_segments = map(lambda x: rbt.Node(x), sorted_segments)

    for i in sorted_segments:
        if i.key.p_type == 0:
            T.insert(i)
            pred = T.predecessor(i)
            if pred and intersect(i.key, i.key.other_end, pred.key, pred.key.other_end):
                return True
            suc = T.successor(i)
            if suc and intersect(i.key, i.key.other_end, suc.key, suc.key.other_end):
                return True
        if i.key.p_type == 1:
            pred = T.predecessor(i)
            suc = T.successor(i)

            if pred and suc:
                if intersect(pred.key, pred.key.other_end, suc.key, suc.key.other_end):
                    return True
            T.delete(i.key)
    return False
    
'''
P1 = [(1,5), (5,4), (2,1), (24,5), (4,2), (13,4), (4,7), (28,3), (12,7), (27,4), (21,12), (26, 1)]
P = [(-0.0416362796235,2.0778654613117),
(2.9990350955684,3.8597407039375),
(2.4995784815943,3.7511631791605),
(-0.1931441328748,5.7272741301016),
(-2.2778326085929,3.7945941890713),
(-1.7792230836344,2.2270202473948),
(-1.5567055008463,2.3441347646517),
(-1.6722033989374,2.9943967149038),
(-1.8601463611155,3.7606257145533),
(0.6553979018846,3.5582256014384)]

points = []
S = []
cont = 0
for i in P:
    if cont % 2 == 0:
        points.append(point.Point(i[0], i[1], p_type=0))
    else:
        points.append(point.Point(i[0], i[1], p_type=1))
    cont += 1

cont = 0
for i in points:
    if cont % 2 == 0:
        S.append(point.Point(i.x, i.y, other_end=points[cont+1]))
    else:
        S.append(point.Point(i.x, i.y, other_end=points[cont-1]))
    cont += 1

print(any_segments_intersect(S))
'''
