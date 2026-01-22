import sys
sys.setrecursionlimit(10**6)

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u != root_v:
        if size[root_u] < size[root_v]:
            parent[root_u] = root_v
            size[root_v] += size[root_u]
            return size[root_v]
        else:
            parent[root_v] = root_u
            size[root_u] += size[root_v]
            return size[root_u]
    return size[root_u]

n, k = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    print(union(a, b))