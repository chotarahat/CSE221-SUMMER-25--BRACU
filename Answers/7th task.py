n =int(input())
ids = list(map(int, input().split()))
marks = list(map(int, input().split()))
sts = list(zip(ids,marks))
swap = 0 

for i in range(n):
    idx= i
    for j in range(i+1,n):
        if sts[j][1]>sts[idx][1]:
            idx = j
        elif sts[j][1] == sts[idx][1] and sts[j][0]< sts[idx][0]:
            idx = j
    if i != idx:
        sts[i],sts[idx] = sts[idx],sts[i]
        swap +=1
print(f"Minimum swaps: {swap}")
for i,marks in sts:
    print(f"ID: {i} Mark: {marks}")      