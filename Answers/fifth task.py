#Task E. Reverse Sorting
def reverse_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

N = int(input())
arr = list(map(int,input().split()))

even = [arr[i] for i in range(N) if i % 2 == 0]
odd = [arr[i] for i in range(N) if i % 2!= 0]
reverse_sort(even)
reverse_sort(odd)

sorted = arr.copy()
reverse_sort(sorted)

even_sorted = [sorted[i] for i in range(N) if i%2 ==0]
odd_sorted = [sorted[i] for i in range(N) if i%2!= 0]


if even == even_sorted and odd == odd_sorted:
    print("YES")
else:
    print("NO")