INF = 10000000000000000000

class Edge:
    def __init__(self, u, v, c, f=0):
        self.source = u
        self.to = v
        self.c = c
        self.f = 0

class PushRelabel:

    def __init__(self, n) -> None:
        self.n = n
        self.m = 0
        self.s = 0
        self.max_bkt = 0
        self.inq = [0]*n
        self.num_h = [0]*(2*n)
        self.cur_e = [0]*n
        self.g = [[] for _ in range(n)]
        self.bkt = [[] for _ in range(2*n)]
        self.ex = [0]*n
        self.edges = []
    
    def add_edge(self, u, v, forward_flow, backward_flow=0) -> int:
        self.g[u].append(self.m)
        self.m += 1
        self.g[v].append(self.m)
        self.m += 1
        self.edges.append(Edge(u, v, forward_flow))
        self.edges.append(Edge(v, u, backward_flow))
        return self.m - 2
    
    def get_edge(self, i) -> Edge:
        return self.edges[i]
    
    def gap_heuristic(self, k):
        for u in range(self.n):
            if (u != self.s and self.h[u] > k and self.h[u] <= self.n):
                self.num_h[self.h[u]] -= 1
                self.cur_e[u] = 0
                if (self.inq[u]):
                    self.bkt[self.h[u]] = []
                    self.bkt[self.n+1].append(u)
                self.h[u] = self.n+1
                self.num_h[self.n+1] += 1
                if (self.h[u] > self.max_bkt):
                    self.max_bkt = self.h[u]
    
    def push(self, u, v, id):
        tmp = min(self.ex[u], self.edges[id].c - self.edges[id].f)
        self.ex[u] -= tmp
        self.ex[v] += tmp
        self.edges[id].f += tmp
        self.edges[id^1].f -= tmp

    def relabel(self, u):
        min_h = 2 * self.n
        for id in self.g[u]:
            if (self.edges[id].f < self.edges[id].c):
                min_h = min(min_h, self.h[self.edges[id].to])
        return 1 + min_h
    
    def discharge(self, u):
        self.inq[u] = 0
        while (self.ex[u] > 0):
            while (self.cur_e[u] < len(self.g[u])):
                id = self.g[u][self.cur_e[u]]
                v = self.edges[id].to
                if (self.edges[id].c == self.edges[id].f):
                    self.cur_e[u] += 1
                    continue
                if (self.h[u] == self.h[v] + 1):
                    self.push(u, v, id)
                    if (self.inq[v] == 0 and v != self.s and v != self.t):
                        self.bkt[self.h[v]].append(v)
                        self.inq[v] = 1
                        if (self.h[v] > self.max_bkt):
                            self.max_bkt = self.h[v]
                if (self.ex[u] == 0): break
                self.cur_e[u] += 1
            if (self.ex[u] > 0):
                prev_h = self.h[u]
                self.num_h[self.h[u]] -= 1
                self.h[u] = self.relabel(u)
                self.num_h[self.h[u]] += 1
                self.cur_e[u] = 0
                if (self.num_h[prev_h] == 0 and prev_h <= self.n - 1):
                    self.gap_heuristic(prev_h)

    def max_flow(self, _s, _t):
        self.s = _s
        self.t = _t
        self.h = [0]*self.n
        self.h[self.s] = self.n
        for id in self.g[self.s]:
            u = self.edges[id].to
            self.ex[u] += self.edges[id].c
            if (self.inq[u] == 0 and u != self.s and u != self.t):
                self.bkt[0].append(u)
                self.inq[u] = 1
            self.edges[id].f += self.edges[id].c
            self.edges[id^1].f -= self.edges[id].c
        while (self.max_bkt >= 0):
            if (len(self.bkt[self.max_bkt]) > 0):
                u = self.bkt[self.max_bkt].pop()
                self.discharge(u)
            else:
                self.max_bkt -= 1
        return self.ex[self.t]

h, n, b = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

# hi = the least we need to get across.
lo = 0
hi = h * h
while hi - lo > 1:
    mid = (hi + lo) // 2
    # Generate all edges where distance^2 <= mid.
    # 0 = source (south)
    # 1 = sink (north)
    # 2x+2 = incoming edges for point x.
    # 2x+3 = outgoing edges for point x.
    pr = PushRelabel(2*n + 2)
    # Part 1: River to point
    for x in range(n):
        diff = points[x][1] * points[x][1]
        if diff <= mid:
            pr.add_edge(0, 2*x+2, 1)
            pr.add_edge(2*x+3, 0, 1)
        diff2 = (h - points[x][1]) * (h - points[x][1])
        if diff2 <= mid:
            pr.add_edge(1, 2*x+2, 1)
            pr.add_edge(2*x+3, 1, 1)
    # Part 2: Point to point
    for x in range(n):
        for y in range(x+1, n):
            diff = (points[x][0] - points[y][0]) * (points[x][0] - points[y][0]) + (points[x][1] - points[y][1]) * (points[x][1] - points[y][1])
            if diff <= mid:
                pr.add_edge(2*x+3, 2*y+2, 1)
                pr.add_edge(2*y+3, 2*x+2, 1)
    # Part 3: In between vertices
    for x in range(n):
        pr.add_edge(2*x+2, 2*x+3, 1)
    # Part 4: River to River
    if mid >= h * h:
        pr.add_edge(0, 1, 100000)
    max_flow = pr.max_flow(0, 1)
    if max_flow >= 2 * b:
        hi = mid
    else:
        lo = mid

# Now find the path, by just moving through adjacent vertices.
pr = PushRelabel(2*n + 2)
# Part 1: River to point
for x in range(n):
    diff = points[x][1] * points[x][1]
    if diff <= hi:
        pr.add_edge(0, 2*x+2, 1)
        pr.add_edge(2*x+3, 0, 1)
    diff2 = (h - points[x][1]) * (h - points[x][1])
    if diff2 <= hi:
        pr.add_edge(1, 2*x+2, 1)
        pr.add_edge(2*x+3, 1, 1)
# Part 2: Point to point
for x in range(n):
    for y in range(x+1, n):
        diff = (points[x][0] - points[y][0]) * (points[x][0] - points[y][0]) + (points[x][1] - points[y][1]) * (points[x][1] - points[y][1])
        if diff <= hi:
            pr.add_edge(2*x+3, 2*y+2, 1)
            pr.add_edge(2*y+3, 2*x+2, 1)
# Part 3: In between vertices
for x in range(n):
    pr.add_edge(2*x+2, 2*x+3, 1)
# Part 4: River to River
if hi >= h * h:
    pr.add_edge(0, 1, 100000)
max_flow = pr.max_flow(0, 1)

assert max_flow >= 2 * b, f"{max_flow} {2 * b}"

seen = [False] * (2*n + 2)
paths = [[None] * (2*n + 2) for _ in range(2 * b)]
for y in range(2 * b):
    current = 0
    cindex = 0
    while True:
        paths[y][cindex] = current
        cindex += 1
        if current == 1:
            break
        if current != 0 and current != 1:
            seen[current] = True
        # Choose an adjacent edge.
        for id in pr.g[current]:
            if pr.edges[id].f > 0 and not seen[pr.edges[id].to]:
                current = pr.edges[id].to
                break
        else:
            break
p = []
for y in range(b):
    p.append("S")
    # Find the rightmost S and leftmost N in the paths.
    l, r = None, None
    for x in range(2 * n + 2):
        if paths[2*y][x] == 0:
            l = x
        elif paths[2*y][x] == 1 and r is None:
            r = x
    for x in range(l+1, r):
        if paths[2*y][x] is not None:
            if paths[2*y][x] % 2 == 0:
                p.append(points[paths[2*y][x] // 2 - 1])
        elif paths[2*y][x] is None:
            break
    p.append("N")
    # Find the rightmost S and leftmost N in the paths.
    l, r = None, None
    for x in range(2 * n + 2):
        if paths[2*y+1][x] == 0:
            l = x
        elif paths[2*y+1][x] == 1 and r is None:
            r = x
    for x in range(r-1, l, -1):
        if paths[2*y+1][x] is not None and paths[2*y+1][x] not in [0, 1]:
            if paths[2*y+1][x] % 2 == 0:
                p.append(points[paths[2*y+1][x] // 2 - 1])
p.append("S")

print(hi, len(p))

for x in p:
    if type(x) == str:
        print(x)
    else:
        print(x[0], x[1])

