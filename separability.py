from graham_scan import graham_scan
from point import Point
from segments_intersect import any_segments_intersect

def make_points(P):
    H = []
    for i in P:
        H.append(Point(i[0], i[1]))
    return H

def get_convex_hull(P):
    H = make_points(P)

    segments_points = []
    segments = []
    hull = graham_scan(H)
    
    for i in hull:
        segments_points.append(Point(i.x, i.y,))
    
    n = len(segments_points)
    for i in range(n):
        segments.append(Point(segments_points[i].x, segments_points[i].y, p_type=0, other_end=segments_points[(i+1)%n]))
        segments.append(Point(segments_points[i].x, segments_points[i].y, p_type=0, other_end=segments_points[(i-1)%n]))
    
    return segments

def separability(H1, H2):
    H = H1 + H2
    return any_segments_intersect(H)

'''
P1 = [(-0.0416362796235,2.0778654613117),
(2.9990350955684,3.8597407039375),
(2.4995784815943,3.7511631791605),
(-0.1931441328748,5.7272741301016),
(-2.2778326085929,3.7945941890713),
(-1.7792230836344,2.2270202473948),
(-1.5567055008463,2.3441347646517),
(-1.6722033989374,2.9943967149038),
(-1.8601463611155,3.7606257145533),
(0.6553979018846,3.5582256014384)]

P2 = [(-4.2557525101923,-0.2573772649794),
(-2.4918882285364,0.2838083668922),
(-2.7324151760349,1.7871017887581),
(-4.6365868437316,2.2080239468805),
(-5.5385628968511,1.9875409116735),
(-4.5564111945655,0.604510963557),
(-3.9350499135276,1.1456965954287),
(-4.8570698789386,1.3461357183441),
(-5.1176407387287,1.6868822273003),
(-4.4962794576908,1.8672774379242)]

P3 = [(4, 0),
(6, 1),
(6.99, 2.57),
(5, 4),
(2, 3),
(1.35, 0.99),
(4, 0)]

P4 = [(1.4675275243176, -0.2507300913821),
(3.2171625600276, 1.23526130881),
(2.8336809083651, 2.8650583283755),
(1.2038838887996, 3.8477300607606),
(-1.0970060211752, 3.3204427897247),
(-1.8400017212713, 1.474937341099),
(1.4675275243176, -0.2507300913821)]

H1 = get_convex_hull(P1)
H2 = get_convex_hull(P2)
H3 = get_convex_hull(P3)
H4 = get_convex_hull(P4)

print(separability(H1, H2))
print(separability(H1, H3))
print(separability(H1, H4))
print(separability(H2, H3))
print(separability(H2, H4))
print(separability(H3, H4))
'''
