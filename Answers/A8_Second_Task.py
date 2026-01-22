import sys
input = sys.stdin.readline

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
    if size[root_u] < size[root_v]:
        parent[root_u] = root_v
        size[root_v] += size[root_u]
    else:
        parent[root_v] = root_u
        size[root_u] += size[root_v]
    return True

n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

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


edges = merge_sort(edges)
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

total_cost = 0
for w, u, v in edges:
    if union(u, v):
        total_cost += w

print(total_cost)