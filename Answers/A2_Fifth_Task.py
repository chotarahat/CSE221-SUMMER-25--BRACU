N, K = map(int, input().split())
arr =list(map(int, input().split()))
left, max_len, sum = 0, 0, 0

for i in range(N):
    sum+= arr[i]

    while sum>K:
        sum -= arr[left]
        left+=1
    max_len = max(max_len, i-left+1)
print(max_len)

#InputCopy
# 5 4
# 4 1 2 1 5
#OutputCopy
#  3