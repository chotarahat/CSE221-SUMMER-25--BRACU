import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)

state = [0] * (N + 1)

def has_cycle():
    for start in range(1, N + 1):
        if state[start] == 0:
            stack = [(start, 0)]
            path = []
            while stack:
                node, idx = stack[-1]
                if state[node] == 0:
                    state[node] = 1
                    path.append(node)
                if idx < len(adj[node]):
                    neighbor = adj[node][idx]
                    stack[-1] = (node, idx + 1)
                    if state[neighbor] == 0:
                        stack.append((neighbor, 0))
                    elif state[neighbor] == 1:
                        return True 
                else:
                    state[node] = 2
                    stack.pop()
                    path.pop()
    return False

print("YES" if has_cycle() else "NO")
