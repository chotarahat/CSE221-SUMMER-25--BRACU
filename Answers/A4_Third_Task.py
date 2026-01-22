
N = int(input())

adj_matrix = [[0] * N for j in range(N)]


for i in range(N):
    parts = list(map(int, input().split()))
    k = parts[0]
    for j in range(1, k + 1):
        adj_matrix[i][parts[j]] = 1


for row in adj_matrix:
    print(' '.join(map(str, row)))