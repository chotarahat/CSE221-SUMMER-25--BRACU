import sys
from collections import deque
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
def reverse(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
N, M, S, D = map(int, input().split())
if N == 1 and M == 0:
    print(0)
    print(1)
    sys.exit()

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

adj = [[] for _ in range(N + 1)]
for u, v in zip(u_list, v_list):
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N + 1):
    merge_sort(adj[i])
visited = [False] * (N + 1)
parent = [-1] * (N + 1)
queue = deque()
queue.append(S)
visited[S] = True

while queue:
    node = queue.popleft()
    if node == D:
        break
    for neighbor in adj[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            queue.append(neighbor)

if not visited[D]:
    print(-1)
else:
    path = []
    cur = D
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    reverse(path)
    print(len(path) - 1)
    print(' '.join(map(str, path)))
