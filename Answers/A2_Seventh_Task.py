n ,q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    start,end = map(int,input().split())
    left, right = 0, n
    while left < right:
        mid = (left+right) // 2
        if arr[mid] < start:
            left = mid + 1
        else:
            right = mid
    L = left

    left, right = 0, n
    while left<right:
        mid = (left+right)//2
        if arr[mid] <= end:
            left = mid + 1
        else:
            right = mid
    R = left

    print(R - L)

#InputCopy
#   5 3
#   10 20 20 45 79
#   20 50
#   5 45
#   1 100
#   OutputCopy
#   3
#   4
#   5