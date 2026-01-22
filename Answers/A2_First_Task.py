N, S = map(int, input().split())
s_list = list(map(int, input().split()))

i = 0
j = N-1


while i < j:
    total= s_list[i]+s_list[j]
    if total == S:
        print(i+1, j+1)
        break
    elif total < S:
        i+=1
    else:
        j -=1
else:
    print(-1)

#  InputCopy
#  4 10
#  1 3 5 7
#  OutputCopy
#  2 4