n, m, q = list(map(int, input().split()))

heights = [list(map(int, input().split())) for _ in range(n)]
# a, b, s
queries = [list(map(int, input().split())) for _ in range(q)]
queries = [[v[1]-1, v[0]-1, v[2], i] for i, v in enumerate(queries)]

queries.sort(key=lambda x: x[2])
solutions = [0]*q

edges = []
for a in range(n):
    for b in range(m):
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = a+dx, b+dy
            if 0 <= x < n and 0 <= y < m:
                edges.append((abs(heights[a][b] - heights[x][y]), a, b, x, y))
edges.sort()

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.A = list(range(n))
        self.s = [1]*n
        self.rank = [0]*n
    
    def find(self, x):
        if self.A[x] != x:
            self.A[x] = self.find(self.A[x])
        return self.A[x]
    
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.A[y] = x
        self.s[x] += self.s[y]
        self.n -= 1
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return self.s[self.find(x)]
    
    def num_sets(self):
        return self.n

uf = UnionFind(n * m)
edge_index = 0
for a, b, s, i in queries:
    while edge_index < len(edges) and edges[edge_index][0] <= s:
        id1 = edges[edge_index][1] * m + edges[edge_index][2]
        id2 = edges[edge_index][3] * m + edges[edge_index][4]
        uf.merge(id1, id2)
        edge_index += 1
    _id = a * m + b
    solutions[i] = uf.size(_id)

for k in solutions:
    print(k)
