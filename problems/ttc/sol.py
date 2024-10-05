class UnionFindWithRollback:

    def __init__(self, n, army_map) -> None:
        self.n = n
        self.A = list(range(n))
        self.size = [1]*n
        self.rank = [0]*n
        self.army_map = army_map
        self.action_stack = []

        self.reverse_map = {}
        for i, army in enumerate(army_map):
            if army not in self.reverse_map:
                self.reverse_map[army] = i
            else:
                self.merge(i, self.reverse_map[army], -1)

    def find(self, x: int) -> int:
        # No path compression - still guaranteed log complexity.
        if self.A[x] != x:
            return self.find(self.A[x])
        return x

    def merge(self, x: int, y: int, time: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        winning_army = self.army_map[x]
        defeated_army = self.army_map[y]
        original_x, original_y = x, y
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.army_map[x] = winning_army

        self.A[y] = x
        self.size[x] += self.size[y]
        self.n -= 1
        rank_increase = False
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
            rank_increase = True
        self.action_stack.append((time, original_x, original_y, winning_army, defeated_army, rank_increase))
        return True

    def undo_until_time(self, time: int):
        while self.action_stack and self.action_stack[-1][0] > time:
            action = self.action_stack.pop()
            x, y, army1, army2, rank_increase = action[1:]
            self.army_map[x] = army1
            self.army_map[y] = army2

            if self.find(x) == y:
                x, y = y, x
            # Now x is on top.
            if rank_increase:
                self.rank[x] -= 1
            self.size[x] -= self.size[y]
            self.A[y] = y

c, q = list(map(int, input().split()))
cities = list(input().split() for _ in range(c))
queries = list(input().split() for _ in range(q))
city_map = {city[0]: index for index, city in enumerate(cities)}

uf = UnionFindWithRollback(c, [x[1] for x in cities])

for query in queries:
    if query[0] == "ATTACK":
        win, lose, year = query[1:]
        uf.merge(uf.reverse_map[win], uf.reverse_map[lose], int(year))
    elif query[0] == "RESET":
        year = query[1]
        uf.undo_until_time(int(year))
    elif query[0] == "DEFENDER":
        city = query[1]
        print(uf.army_map[uf.find(city_map[city])])
