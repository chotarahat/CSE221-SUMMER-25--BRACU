def merge(a, b):
    i,j, inv_c = 0, 0, 0
    c = []
    while i <len(a) and j<len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            inv_c +=len(a) -i
            j+=1
    while i<len(a):
        c.append(a[i])
        i+=1
    while j<len(b):
        c.append(b[j])
        j+=1
    return c,inv_c

def mergeSort(arr):
    if len(arr)<=1:
        return arr,0
    else:
        mid = len(arr)//2
        a1 ,inv_left = mergeSort(arr[:mid])
        a2, inv_right = mergeSort(arr[mid:])
        merged , inv_merge = merge(a1,a2)
        return merged, inv_left + inv_right + inv_merge
N = int(input())
arr= list(map(int, input().split()))  
sorted_arr, inv_count =mergeSort(arr)
print(inv_count)
print(*sorted_arr)       