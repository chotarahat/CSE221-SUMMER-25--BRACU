def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
N, Q = map(int, input().split())
 
neighbors = [[] for _ in range(N + 1)]
 
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and gcd(i, j) == 1:
            neighbors[i].append(j)
    neighbors[i].sort()
 
for _ in range(Q):
    X, K = map(int, input().split())
    if K <= len(neighbors[X]):
        print(neighbors[X][K - 1])
    else:
        print(-1)
