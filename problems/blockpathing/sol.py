from math import sqrt, atan2, pi, acos, sin, cos
from heapq import heappush, heappop, heapify

start = list(map(int, input().split()))
end = list(map(int, input().split()))
rect = sx, sy, ex, ey = list(map(int, input().split()))
radius, cx, cy = list(map(int, input().split()))

EPS = pow(10, -6)

DEBUG = False

def point_in_rectangle(x, y, equal=False):
    if equal:
        return min(sx, ex) - EPS <= x <= max(sx, ex) + EPS and min(sy, ey) - EPS <= y <= max(sy, ey) + EPS
    return min(sx, ex) + EPS < x < max(sx, ex) - EPS and min(sy, ey) + EPS < y < max(sy, ey) - EPS

def line_intersects_rectangle(x1, y1, x2, y2):
    if point_in_rectangle(x1, y1) or point_in_rectangle(x2, y2):
        return True
    # Handle the case where both points are on the boundary:
    if x1 in [sx, ex] and x2 in [sx, ex] and y1 in [sy, ey] and y2 in [sy, ey]:
        return not (x1 == x2 or y1 == y2)
    # And now the general case, where two distinct intersection points is the smoking gun.
    intersections = set()
    for xp in (sx, ex):
        if min(x1, x2) <= xp <= max(x1, x2):
            # interp to line point
            if x1 == x2:
                ypos = y1
            else:
                ypos = y2 + (y1-y2) * ((x2-xp)/(x2-x1))
            if point_in_rectangle(xp, ypos, True):
                intersections.add((xp, ypos))
    for yp in (sy, ey):
        if min(y1, y2) <= yp <= max(y1, y2):
            # interp to line point
            if y1 == y2:
                xpos = x1
            else:
                xpos = x2 + (x1-x2) * ((y2-yp)/(y2-y1))
            if point_in_rectangle(xpos, yp, True):
                intersections.add((xpos, yp))
    if DEBUG:
        print(intersections)
    return len(intersections) > 1

def point_in_circle(x, y, equal=False):
    if equal:
        return (x-cx)**2 + (y-cy)**2 <= radius**2 + EPS
    return (abs(x-cx) + EPS)**2 + (abs(y-cy) + EPS)**2 < radius**2

def line_intersects_circle(x1, y1, x2, y2):
    if point_in_circle(x1, y1) or point_in_circle(x2, y2):
        return True
    # Only way we are closer is the normal intersection is somewhere in the middle of the line
    normal_gradient = y1 - y2, x2 - x1
    # line equation for original: line1[0]*x + line1[1]*y + line1[2] = 0
    line1 = y2 - y1, x1 - x2, y1*x2 - x1*y2
    # line equation for normal: line2[0]*x + line2[1]*y + line2[2] = 0
    line2 = normal_gradient[1], -normal_gradient[0], - cx * normal_gradient[1] + cy * normal_gradient[0]
    # intersection
    intersection_point = (
        (line1[1]*line2[2] - line2[1]*line1[2]) / (line1[0]*line2[1] - line2[0]*line1[1]),
        (line2[0]*line1[2] - line1[0]*line2[2]) / (line1[0]*line2[1] - line2[0]*line1[1])
    )
    # print(line1, line2, intersection_point)
    return (
        point_in_circle(*intersection_point) and
        min(x1, x2) <= intersection_point[0] <= max(x1, x2) and
        min(y1, y2) <= intersection_point[1] <= max(y1, y2)
    )

def tangent_points(x, y):
    if (x-cx)**2 + (y-cy)**2 == radius**2:
        # On Radius
        return (x, y), None
    if point_in_circle(x, y):
        return (None, None)
    to_centre = x-cx, y-cy
    centre_dist = sqrt(to_centre[0]**2 + to_centre[1]**2)
    norm_centre = to_centre[0]/centre_dist, to_centre[1]/centre_dist
    angle = acos(radius / centre_dist)
    rotated1 = (
        cos(angle)*norm_centre[0] - sin(angle)*norm_centre[1],
        sin(angle)*norm_centre[0] + cos(angle)*norm_centre[1]
    )
    rotated2 = (
        cos(-angle)*norm_centre[0] - sin(-angle)*norm_centre[1],
        sin(-angle)*norm_centre[0] + cos(-angle)*norm_centre[1]
    )
    return (cx + rotated1[0]*radius, cy + rotated1[1]*radius), (cx + rotated2[0]*radius, cy + rotated2[1]*radius)



interesting_points = [
    start,
    end,
    (sx, sy),
    (ex, sy),
    (sx, ey),
    (ex, ey),
]
# Compute tangents
tangents = []
for point in interesting_points:
    tangent1, tangent2 = tangent_points(*point)
    if tangent1 is not None:
        tangents.append(tangent1)
    if tangent2 is not None:
        tangents.append(tangent2)
if DEBUG:
    print("POINTS")
    print(interesting_points)
    print(tangents)
distance = [
    [None for _ in range(len(interesting_points) + len(tangents))]
    for _ in range(len(interesting_points) + len(tangents))
]
# Easily compute distance between tangent points.
for i1, t1 in enumerate(tangents, start=len(interesting_points)):
    for i2, t2 in enumerate(tangents, start=len(interesting_points)):
        if i1 == i2:
            distance[i1][i2] = 0
        vec1 = (t1[0]-cx, t1[1]-cy)
        vec2 = (t2[0]-cx, t2[1]-cy)
        angle = atan2(vec1[1]*vec2[0]-vec1[0]*vec2[1], vec1[0]*vec2[0] + vec1[1]*vec2[1])
        if angle > pi:
            angle -= 2*pi
        if angle < -pi:
            angle += 2*pi
        d = radius * abs(angle)
        distance[i1][i2] = d
# Compute distance / feasibility from all pairs of interesting points.
all_points = interesting_points + tangents
for i1, t1 in enumerate(all_points):
    for i2, t2 in enumerate(all_points):
        if distance[i1][i2] != None:
            continue
        if i1 == i2 or tuple(t1) == tuple(t2):
            distance[i1][i2] = 0
            continue
        # Straight line
        if line_intersects_rectangle(*t1, *t2):
            continue
        if line_intersects_circle(*t1, *t2):
            continue
        d = sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2)
        distance[i1][i2] = d

# Now just do dijkstras from start to end.
point_heap = []
heapify(point_heap)
# Heap elements: distance, index.
marked = [False] * len(all_points)
parent = [-1] * len(all_points)
heappush(point_heap, (0, 0, -1))
while point_heap:
    dist, index, par = heappop(point_heap)
    if marked[index]:
        continue
    marked[index] = True
    parent[index] = par
    for neighbour in range(len(all_points)):
        if distance[index][neighbour] is not None and not marked[neighbour]:
            heappush(point_heap, (dist + distance[index][neighbour], neighbour, index))

# End should be marked.
if not marked[1]:
    raise ValueError("WTF")
points = []
current = 1
while current != -1:
    points.append(current)
    current = parent[current]
path = points[::-1]

if DEBUG:
    print([all_points[i] for i in path])
    for p1, p2 in zip(path[:-1], path[1:]):
        p1, p2 = all_points[p1], all_points[p2]
        line1 = p2[1] - p1[1], p1[0] - p2[0], p1[1]*p2[0] - p1[0]*p2[1]
        print(line1)
total_distance = sum(distance[i][j] for (i, j) in zip(points[:-1], points[1:]))
print(total_distance)

# print("\n".join(f"{i}: {all_points[i]}" for i in range(len(all_points))))
