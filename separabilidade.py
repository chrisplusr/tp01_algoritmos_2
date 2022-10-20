from graham_scan import graham_scan
from point import Point
from segments_intersect import any_segments_intersect

def make_points(P):
    H = []
    for i in P:
        H.append(Point(i[0], i[1]))
    return H

def hull_segments(P):
    H = make_points(P)

    segments_points = []
    segments = []
    hull = graham_scan(H)
    hull.append(hull[0])

    count = 0
    for i in hull:
        if count % 2 == 0:
            segments_points.append(Point(i.x, i.y, 0))
        else:
            segments_points.append(Point(i.x, i.y, 1))
        count += 1
    
    count = 0
    for i in segments_points:
        if count % 2 == 0:
            segments.append(Point(i.x, i.y, 0, other_end=segments_points[count+1]))
        else:
            segments.append(Point(i.x, i.y, 1, other_end=segments_points[count-1]))
        count += 1
    
    return segments

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

H = hull_segments(P1)
print(any_segments_intersect(H))
'''
for i in H:
    print(i, i.p_type)
'''
