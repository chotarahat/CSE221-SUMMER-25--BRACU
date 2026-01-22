from collections import defaultdict
import heapq

def ancient_ordering():
    N = int(input())
    words = []
    for _ in range(N):
        word = input().strip()
        words.append(word)

    graph = defaultdict(set)
    in_degree = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    present = set()

    for word in words:
        present.update(word)

    for i in range(N - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        found = False

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                found = True
                break

        if not found and len(w1) > len(w2):
            print("-1")
            return
    heap = [c for c in in_degree if in_degree[c] == 0 and c in present]
    heapq.heapify(heap)
    result = []

    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        for v in sorted(graph[u]):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    if len(result) != len(present):
        print("-1")
    else:
        print(''.join(result))

ancient_ordering()
