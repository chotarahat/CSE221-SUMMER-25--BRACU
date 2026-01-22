N = int(input())
x, y = map(int, input().split())


directions = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1)]


valid_moves = []
for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        valid_moves.append((nx, ny))

for i in range(len(valid_moves)):
    min_idx = i
    for j in range(i + 1, len(valid_moves)):
        if valid_moves[j][0] < valid_moves[min_idx][0] or \
           (valid_moves[j][0] == valid_moves[min_idx][0] and valid_moves[j][1] < valid_moves[min_idx][1]):
            min_idx = j
    valid_moves[i], valid_moves[min_idx] = valid_moves[min_idx], valid_moves[i]


print(len(valid_moves))
for i in valid_moves:
    print(i[0], i[1])