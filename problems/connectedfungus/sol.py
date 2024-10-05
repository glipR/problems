class LCA:
    """
    vertices are represented as numbers 0->n-1.
    """

    # number such that 2^{MAX_LOG} > n. 20 works for n <= 10^6.
    MAX_LOG = 20

    def __init__(self, n_vertices):
        self.n = n_vertices
        self.adjacent = [[] for _ in range(self.n)]

    def add_edge(self, u, v, weight=1):
        self.adjacent[u].append((v, weight))
        self.adjacent[v].append((u, weight))

    def dfs(self, source, c_parent, c_level, c_length):
        # Search from the source down the tree and set parent, level, length accordingly.
        self.parent[source] = c_parent
        self.level[source] = c_level
        self.length[source] = c_length
        for child, weight in self.adjacent[source]:
            if child != c_parent:
                self.dfs(child, source, c_level + 1, c_length + weight)

    def build(self, root):
        # Once edges are added, build the tree/data structure.
        self.parent = [None]*self.n
        self.level = [None]*self.n
        self.length = [None]*self.n
        self.n_verts = [0]*self.n
        self.sum_d = [0]*self.n
        self.sum_sq = [0]*self.n
        self.alive = [False] * self.n
        self.dfs(root, -1, 0, 0)
        self.ancestor = [[-1]*self.MAX_LOG for _ in range(self.n)]
        # Initial step: ancestor[v][0] = parent[v]
        for v in range(self.n):
            self.ancestor[v][0] = self.parent[v]
        # Now, compute ancestor[v][k] from 1->MAX_LOG
        for k in range(1, self.MAX_LOG):
            for v in range(self.n):
                if self.ancestor[v][k-1] != -1:
                    # Move 2^{k-1} up, then 2^{k-1} again.
                    self.ancestor[v][k] = self.ancestor[self.ancestor[v][k-1]][k-1]

    def update_upwards(self, v, depth=None):
        if depth == None:
            depth = self.level[v]
            self.alive[v] = True
        self.n_verts[v] += 1
        self.sum_d[v] += depth
        self.sum_sq[v] += depth * depth
        if self.parent[v] != -1:
            self.update_upwards(self.parent[v], depth)

    def query(self, u, v, root=None):
        # What is the lowest common ancestor of u, v?
        # Extension: Make this query from any root vertex you want.
        if root is not None:
            # NEW: Custom root -- see diagrams below for reasoning.
            a = self.query(u, v)
            b = self.query(u, root)
            c = self.query(v, root)
            # Case 1: root is in the same component as u when `a` is removed from the tree. So `b` is the LCA
            if (a == c and c != b): return b
            # Case 2: root is in the same component as v when `a` is removed from the tree. So `a` is the LCA
            if (a == b and c != b): return c
            # Case 3: b and c are above a in the tree. So return a
            return a
        # assume that u is higher up than v, to simplify the code below
        if self.level[u] > self.level[v]:
            u, v = v, u
        # STEP 1: set u and v to be ancestors with the same level
        for k in range(self.MAX_LOG-1, -1, -1):
            if (self.level[v] - (1 << k) >= self.level[u]):
                # If v is 2^k levels below u, move it up 2^k levels.
                v = self.ancestor[v][k]
        # We can be certain that level[u] = level[v]. Reason: binary representation of all natural numbers.
        # Do we need to move to step 2?
        if (u == v): return u
        # STEP 2: find the highest ancestor where u != v. Then the parent is the LCA
        for k in range(self.MAX_LOG-1, -1, -1):
            if (self.ancestor[u][k] != self.ancestor[v][k]):
                # Move up 2^k steps
                u = self.ancestor[u][k]
                v = self.ancestor[v][k]
        return self.parent[u]

    def dist(self, u, v):
        return self.length[u] + self.length[v] - 2 * self.length[self.query(u, v)]

    def alive_ancestor(self, v):
        if self.parent[v] == -1 or not self.alive[self.parent[v]]:
            return v
        return self.alive_ancestor(self.parent[v])

    def sum_anc(self, v):
        prev = None
        cur = v
        acc = 0
        if not self.alive[cur] and self.parent[cur] != -1:
            prev = cur
            cur = self.parent[cur]
        while cur != -1 and self.alive[cur]:
            acc += self.level[cur] * self.n_verts[cur]
            if prev is not None:
                acc -= self.level[cur] * self.n_verts[prev]
            prev = cur
            cur = self.parent[cur]
        return acc
    
    def sum_anc_sq(self, v):
        prev = None
        cur = v
        acc = 0
        if not self.alive[cur] and self.parent[cur] != -1:
            prev = cur
            cur = self.parent[cur]
        while cur != -1 and self.alive[cur]:
            acc += self.level[cur] * self.level[cur] * self.n_verts[cur]
            if prev is not None:
                acc -= self.level[cur] * self.level[cur] * self.n_verts[prev]
            prev = cur
            cur = self.parent[cur]
        return acc

    def sum_anc_dj(self, v):
        prev = None
        cur = v
        acc = 0
        if not self.alive[cur] and self.parent[cur] != -1:
            prev = cur
            cur = self.parent[cur]
        while cur != -1 and self.alive[cur]:
            acc += self.sum_d[cur]
            prev = cur
            cur = self.parent[cur]
        if prev is not None:
            acc += self.sum_d[prev] * (self.level[prev]-1)
        return acc

MOD = 10**9 + 7

t = int(input())
for i in range(t):
    largest_group = 0
    most_alive_children = 0
    longest_path = 0
    x, n = map(int, input().split())
    L = LCA(n)
    for edge in range(n-1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        L.add_edge(a, b, c)
    L.build(0)
    # Now, we need to simulate, and spot when everything gets infected.
    LIVE = 0
    DIE = 1
    events = [(0, 0, LIVE), (x, 0, DIE)]
    marked = [False]*n
    marked[0] = True
    queue = [(0, 0)]
    while queue:
        node, live = queue.pop()
        for adj in L.adjacent[node]:
            if not marked[adj[0]]:
                marked[adj[0]] = True
                queue.append((adj[0], live + adj[1]))
                events.append((live + adj[1], adj[0], LIVE))
                events.append((live + adj[1] + x, adj[0], DIE))
    events.sort()
    # Now we can handle events in order.
    total_work = 0
    current_work = 0
    ctime = 0
    while events:
        event = events.pop(0)
        node = event[1]
        time = event[0]
        state = event[2]
        if time > ctime:
            # We are simulating the day at our current time, up until this event.
            total_work += (current_work * ((time - ctime)%MOD)) % MOD
            total_work %= MOD
            # print(current_work, "at", ctime, "to", time)
            ctime = time
        # Now, how does this change the current work?
        if state == LIVE:
            anc = L.alive_ancestor(node)
            largest_group = max(largest_group, L.n_verts[anc])
            longest_path = max(longest_path, L.level[node] - L.level[anc])
            # print("Adding", node)
            # First effect, d_i^2 for every vertex we are connected to.
            current_work += L.n_verts[anc] * L.level[node] * L.level[node]
            # Second effect, sum of all dj^2.
            current_work += L.sum_sq[anc]
            # Third effect, 4 * LCA(i,j)^2
            current_work += 4 * L.sum_anc_sq(node)
            # Fourth effect, 4 * di * lca(i, j)
            current_work -= 4 * L.level[node] * L.sum_anc(node)
            # Fifth effect, 4 * dj * lca(i, j)
            current_work -= 4 * L.sum_anc_dj(node)
            # Sixth effect, 2 * di * dj
            current_work += 2 * L.level[node] * L.sum_d[anc]
            current_work %= MOD
            # Now include node in our newer calculations.
            L.update_upwards(node)
        else:
            # print("Ending", node)
            # STEP 1, lets remove node from our calculations.
            L.alive[node] = False
            L.n_verts[node] -= 1
            L.sum_d[node] -= L.level[node]
            L.sum_sq[node] -= L.level[node] * L.level[node]
            # First effect, d_i^2 for every vertex we are connected to.
            current_work -= L.n_verts[node] * L.level[node] * L.level[node]
            # Second effect, sum of all dj^2.
            current_work -= L.sum_sq[node]
            # Third effect, 4 * LCA(i,j)^2, which is just the highest alive ancestor.
            current_work -= 4 * L.level[node] * L.level[node] * L.n_verts[node]
            # Fourth effect, 4 * di * lca(i, j)
            current_work += 4 * L.level[node] * L.level[node] * L.n_verts[node]
            # Fifth effect, 4 * dj * lca(i, j)
            current_work += 4 * L.level[node] * L.sum_d[node]
            # Sixth effect, 2 * di * dj
            current_work -= 2 * L.level[node] * L.sum_d[node]
            current_work %= MOD
            # STEP 2, now we deal with separate components being disconnected.
            al = 0
            for adj in L.adjacent[node]:
                if L.parent[adj[0]] == node and L.alive[adj[0]]:
                    al += 1                    
                    # Deal with the coefficients where di is a factor.
                    # First effect, d_i^2 for every vertex we are connected to.
                    current_work -= L.sum_sq[adj[0]] * (L.n_verts[node] - L.n_verts[adj[0]])
                    # Second effect, 2 * sum of all lca^2.
                    current_work -= 2 * L.n_verts[adj[0]] * (L.n_verts[node] - L.n_verts[adj[0]]) * L.level[node] * L.level[node]
                    # Third effect, 4 * di * lca(i, j)
                    current_work += 4 * L.sum_d[adj[0]] * L.level[node] * (L.n_verts[node] - L.n_verts[adj[0]])
                    # Fourth effect, di * dj
                    current_work -= L.sum_d[adj[0]] * (L.sum_d[node] - L.sum_d[adj[0]])
                    current_work %= MOD
            most_alive_children = max(most_alive_children, al)
    print(total_work)#, largest_group, most_alive_children, longest_path)
