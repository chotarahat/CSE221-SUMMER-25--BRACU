N,M,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i ,j = 0, M-1
based_i , based_j = 0, 0
min_diff = float('inf')

while i < N and j>=0:
    sum = A[i] + B[j]
    diff = abs(sum -K)
    if diff < min_diff:
        min_diff = diff
        based_i ,based_j = i,j
    if sum <K:
        i+= 1
    else:
        j -= 1
print(based_i +1, based_j+1)


#   InputCopy
#   4 4 0
#   -5 -2 -1 5
#   -5 0 1 1
#   OutputCopy
#   3 4