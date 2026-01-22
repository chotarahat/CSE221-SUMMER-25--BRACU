import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict, deque

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        return False
    parent[root_v] = root_u
    return True

def merge_sort(edges):
    if len(edges) <= 1:
        return edges
    mid = len(edges) // 2
    left = merge_sort(edges[:mid])
    right = merge_sort(edges[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges = merge_sort(edges)

parent = [i for i in range(n + 1)]
mst_edges = []
mst_cost = 0

for w, u, v in edges:
    if union(u, v):
        mst_edges.append((u, v, w))
        mst_cost += w


graph = defaultdict(list)
for u, v, w in mst_edges:
    graph[u].append((v, w))
    graph[v].append((u, w))


LOG = math.ceil(math.log2(n)) + 1
up = [{} for _ in range(LOG)]
max_edge = [{} for _ in range(LOG)]
depth = [0] * (n + 1)

def dfs(u, p):
    for v, w in graph[u]:
        if v != p:
            depth[v] = depth[u] + 1
            up[0][v] = u
            max_edge[0][v] = w
            dfs(v, u)

dfs(1, -1)


for k in range(1, LOG):
    for v in range(1, n + 1):
        if v in up[k - 1]:
            prev = up[k - 1][v]
            if prev in up[k - 1]:
                up[k][v] = up[k - 1][prev]
                max_edge[k][v] = max(max_edge[k - 1][v], max_edge[k - 1][prev])

def get_max_edge(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    res = 0
    for k in reversed(range(LOG)):
        if depth[u] - (1 << k) >= depth[v]:
            res = max(res, max_edge[k][u])
            u = up[k][u]
    if u == v:
        return res
    for k in reversed(range(LOG)):
        if up[k][u] != -1 and up[k][u] != up[k][v]:
            res = max(res, max_edge[k][u], max_edge[k][v])
            u = up[k][u]
            v = up[k][v]
    return max(res, max_edge[0][u], max_edge[0][v])


mst_set = set((min(u, v), max(u, v)) for u, v, w in mst_edges)
second_best = float('inf')

for w, u, v in edges:
    if (min(u, v), max(u, v)) not in mst_set:
        max_w = get_max_edge(u, v)
        new_cost = mst_cost - max_w + w
        if new_cost > mst_cost:
            second_best = min(second_best, new_cost)

print(second_best if second_best != float('inf') else -1)