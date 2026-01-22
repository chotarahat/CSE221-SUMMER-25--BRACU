cases = int(input())
for i in range(cases):
    k,x = map(int, input().split())
    print(k +(k-1)//(x-1))

#InputCopy
#   6
#   7 3
#   100 5
#   49 13
#   36 2
#   1 2
#   11 11
#   OutputCopy
#   10
#   124
#   53
#   71
#   1
#   12