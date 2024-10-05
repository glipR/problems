from queue import Queue

class BipartiteMatchingCapacity:
    
    def __init__(self, L, R, cap=1):
        self.L = L
        self.R = R
        self.d = [0] * (R+1)
        self.adj = [[] for _ in range(R)]
        self.capacity_r = [cap] * R
        self.capacity_l = [cap] * L
        self.q = Queue()
        self.p = 0
        self.m = []
        self.used = []

    def add_edge(self, u, v):
        self.adj[v].append(u)
    
    def bfs(self) -> bool:
        for v in range(self.R):
            if (self.used[v] < self.capacity_r[v]):
                self.d[v] = self.p
                self.q.put(v)
        while not (self.q.empty()):
            v = self.q.get()
            if (self.d[v] != self.d[self.R]):
                for u in self.adj[v]:
                    if v in self.m[u]:
                        continue
                    for nv in self.m[u]:
                        if self.d[nv] < self.p:
                            self.d[nv] = self.d[v] + 1
                            self.q.put(nv)
        return self.d[self.R] >= self.p
    
    def dfs(self, v):
        if (v == self.R):
            return 1
        for u in self.adj[v]:
            if v not in self.m[u]:
                for nv in self.m[u]:
                    if (self.d[nv] == self.d[v] + 1) and self.dfs(nv):
                        self.m[u].append(v)
                        if nv != self.R or len(self.m[u]) > self.capacity_l[u]:
                            self.m[u].remove(nv)
                        return 1
        self.d[v] = self.d[self.R]
        return 0

    def match(self):
        res = 0
        self.m = [[self.R] for _ in range(self.L)]
        self.used = [0] * (self.R + 1)
        self.p = 0
        while True:
            if not self.bfs():
                break
            for v in range(self.R):
                if (self.used[v] < self.capacity_r[v]) and self.dfs(v):
                    self.used[v] += 1
                    res += 1
            self.p = self.d[self.R] + 1
        for x in range(len(self.m)):
            if self.m[x] == self.R:
                self.m[x] = -1
        return res, self.m

c, d, p = list(map(int, input().split()))
pairings = []
for x in range(p):
    c1, d1 = list(map(int, input().split()))
    pairings.append((c1-1, d1-1))

bm = BipartiteMatchingCapacity(c, d, 2)
for c1, d1 in pairings:
    bm.add_edge(c1, d1)

res, m = bm.match()
if res == 2*c and c == d:
    print("YES")
    for x in range(c):
        print(f"Cat #{x+1} sits with Dog #{m[x][0]+1} and Dog #{m[x][1]+1}")
else:
    print("NO")
