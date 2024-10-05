import sys
sys.setrecursionlimit(50000)

TESTING = False

if TESTING:
    class CheckerResult:
        def __init__(self, *args, **kwargs) -> None:
            self.args = args
            self.kwargs = kwargs

        def __repr__(self) -> str:
            return f"Result. args:{self.args}, kwargs:{self.kwargs}"
else:
    from dmoj.result import CheckerResult

def remove_edge(adj_list, x, y):
    """Remove the edge between x and y"""
    for n, d in adj_list[x]:
        if n == y:
            adj_list[x].remove((n, d))
            break
    for n, d in adj_list[y]:
        if n == x:
            adj_list[y].remove((n, d))
            break

def add_edge(adj_list, x, y, d):
    adj_list[x].append((y, d))
    adj_list[y].append((x, d))

def build_tree(actions):
    adj_list = [[]]
    next_n = 1
    move_stack = [] # Current path in the tree.
    for action, dist in actions:
        d = int(dist)
        if action == "TUNNEL":
            if move_stack:
                prev_n = move_stack[-1][0]
            else:
                prev_n = 0
            move_stack.append((next_n, d))
            adj_list.append([])

            add_edge(adj_list, prev_n, next_n, d)

            next_n += 1
        elif action == "BACK":
            prev_dist = move_stack[-1][1] if move_stack else 0
            while d >= prev_dist and prev_dist != 0:
                move_stack.pop()
                d -= prev_dist
                prev_dist = move_stack[-1][1] if move_stack else 0
            if d == 0:
                continue
            if prev_dist == 0:
                raise ValueError()
            # Sub-distance. Break apart the current path and add intermediary node.
            forward_node = move_stack[-1][0]
            if len(move_stack) >= 2:
                root_node = move_stack[-2][0]
            else:
                root_node = 0

            adj_list.append([])

            remove_edge(adj_list, root_node, forward_node)
            add_edge(adj_list, root_node, next_n, prev_dist - d)
            add_edge(adj_list, forward_node, next_n, d)

            move_stack.pop()
            move_stack.append((next_n, prev_dist - d))

            next_n += 1


    # Next, flatten the tree so there are no degree 2 nodes.
    # Skip x==0 because that's the root node.
    to_flatten = [x for x in range(1, len(adj_list)) if len(adj_list[x]) == 2]
    for x in to_flatten:
        (n1, d1), (n2, d2) = adj_list[x]
        total_d = d1 + d2
        remove_edge(adj_list, n1, x)
        remove_edge(adj_list, x, n2)
        add_edge(adj_list, n1, n2, total_d)

    # This may have some empty lists and the nodes aren't dense but idm
    return adj_list

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures funrace solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    # judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")

    judge_n = int(inp[0])
    judge_lines = list(map(lambda x: map(int, x.split()), inp[1:judge_n]))

    try:
        proc_n = int(process[0])
        proc_inst = [process[x].split() for x in range(1, proc_n+1)]
    except:
        return CheckerResult(False, 0, "Invalid output format")

    try:
        proc_tree = build_tree(proc_inst)
    except:
        return CheckerResult(False, 0, "Invalid output")

    node_mapping = {0:0}
    judge_adj_list = [[] for _ in range(judge_n)]
    for x, y, d in judge_lines:
        add_edge(judge_adj_list, x-1, y-1, d)

    def dfs(cur_node):
        # Since we know that node 0 in both examples are the same
        # Just form the test data so that no two neighours have the same distance
        # Then we can match them up easily
        judge_adj = judge_adj_list[cur_node][:]
        process_adj = proc_tree[node_mapping[cur_node]][:]

        assert len(judge_adj) == len(process_adj), "Number of nodes differs."
        to_remove_judge = set()
        for x, d in judge_adj:
            if x in node_mapping:
                to_remove_judge.add((x, d))
        to_remove_proc = set()
        for x, d in process_adj:
            if x in node_mapping.values():
                to_remove_proc.add((x, d))
        assert len(to_remove_proc) == len(to_remove_judge), "Number of parent nodes should be 0 or 1."
        for x in to_remove_judge:
            judge_adj.remove(x)
        for x in to_remove_proc:
            process_adj.remove(x)

        # Now just new nodes.
        judge_dist_map = {
            d:x
            for x, d in judge_adj
        }
        proc_dist_map = {
            d:x
            for x, d in process_adj
        }
        assert len(judge_dist_map) == len(proc_dist_map), 'Different amount of distances'
        judge_keys = list(sorted(judge_dist_map.keys()))
        proc_keys = list(sorted(proc_dist_map.keys()))
        for judge_d, proc_d in zip(judge_keys, proc_keys):
            assert judge_d == proc_d, 'Distances different'
            node_mapping[judge_dist_map[judge_d]] = proc_dist_map[proc_d]
            dfs(judge_dist_map[judge_d])

    try:
        dfs(0)
    except AssertionError:
        return CheckerResult(False, 0, feedback="Hill created is incorrect.")


    return CheckerResult(True, kwargs["point_value"])

if __name__ == "__main__":
    test_path = sys.argv[1]
    with open(test_path, "r") as f:
        inp_test = f.read()
    with open(test_path.replace(".in", ".out"), "r") as f:
        out_test = f.read()
    print(check(out_test.encode("utf-8"), out_test.encode("utf-8"), judge_input=inp_test.encode("utf-8"), point_value=1))
