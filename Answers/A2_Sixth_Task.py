N, K= map(int, input().split())
arr = list(map(int, input().split()))

n_arr = [0]*(N+1)
left,elem,max_len = 0, 0, 0

for i in range(N):
    if n_arr[arr[i]] == 0:
        elem+=1
    n_arr[arr[i]] += 1

    while elem>K:
        n_arr[arr[left]] -=1
        if n_arr[arr[left]] == 0:
            elem -=1
        left+=1
    max_len = max(max_len, i-left+1)
print(max_len)

#InputCopy
#   4 1
#   2 1 2 4
#   OutputCopy
#   1