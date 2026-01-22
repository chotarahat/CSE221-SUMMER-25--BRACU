import sys
sys.setrecursionlimit(3 * 10**5)
input = sys.stdin.readline

N, R = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

subtree_size = [0] * (N + 1)

def dfs(u, parent):
    size = 1
    for v in adj[u]:
        if v != parent:
            size += dfs(v, u)
    subtree_size[u] = size
    return size

dfs(R, -1)

Q = int(input())
for _ in range(Q):
    X = int(input())
    print(subtree_size[X])
