N = int(input())
alice = list(map(int, input().split()))
M = int(input())
bob = list(map(int, input().split()))
arr = []
i,j =0, 0
while i <N and j<M:
    if alice[i]<= bob[j]:
        arr.append(alice[i])
        i+=1
    else:
        arr.append(bob[j])
        j+=1
while i<N:
    arr.append(alice[i])
    i+=1
while j<M:
    arr.append(bob[j])
    j+=1
print(*arr)

#InputCopy
#    4
#    1 3 5 7
#    4
#    2 2 4 8
#    OutputCopy
#    1 2 2 3 4 5 7 8 