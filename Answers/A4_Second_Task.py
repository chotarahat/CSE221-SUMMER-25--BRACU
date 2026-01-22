# TASK B: Adjacency List Representation

nodes, edge = map(int, input().split())
start_points = list(map(int, input().split()))
end_points = list(map(int, input().split()))
weights = list(map(int, input().split()))

adj_list = [[] for _ in range(nodes + 1)]

for i in range(edge):
    u = start_points[i]
    v = end_points[i]
    w = weights[i]
    adj_list[u].append((v, w))

for i in range(1, nodes + 1):
    print(f"{i}:", end="")
    for v, w in adj_list[i]:
        print(f" ({v},{w})", end="")
    print()