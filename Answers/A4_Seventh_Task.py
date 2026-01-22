N, M, K = map(int, input().split())

knights = set()
for _ in range(K):
    x, y = map(int, input().split())
    knights.add((x, y))

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

found = False
for x, y in knights:
    for dx, dy in moves:
        if (x + dx, y + dy) in knights:
            found = True
            break
    if found:
        break

print("YES" if found else "NO")