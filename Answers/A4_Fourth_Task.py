N, M = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))

degree = [0] * (N + 1) 

for i in range(M):
    degree[u[i]] += 1
    degree[v[i]] += 1


odd_count = 0
for i in range(1, len(degree)):
    if degree[i] % 2 == 1:
        odd_count += 1

if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")
