def triple():
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        dic = {}
        remain = x - arr[i]
        for j in range(i + 1, n):
            third_value = remain - arr[j]
            if third_value in dic and dic[third_value] != i and dic[third_value] != j:
                print(i+1, dic[third_value]+1, j+1)
                return
            dic[arr[j]] = j
    print(-1)
triple()


#   InputCopy
#   7 3
#   2 1 1 2 2 1 1
#   OutputCopy
#   2 3 6 