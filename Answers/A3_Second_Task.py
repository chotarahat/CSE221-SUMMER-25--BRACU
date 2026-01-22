def count(sorted_list, x):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2  
        if sorted_list[mid] < x:
            low = mid + 1  
        else:
            high = mid - 1 
    return low 

def merge_and_count(my_arr, start, middle, end):
    total_count = 0
  
    left = []
    for i in range(start, middle + 1):
        left.append(my_arr[i])
    
    right = []
    for i in range(middle + 1, end + 1):
        right.append(my_arr[i])

  
    squared_right = []
    for m in right:
        squared_right.append(m * m) 
    squared_right.sort() 

    
    for n in left:
        total_count += count(squared_right, n)

    
    i = 0 
    j = 0  
    k = start 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            my_arr[k] = left[i]
            i = i + 1
        else:
            my_arr[k] = right[j]
            j = j + 1
        k = k + 1
    
    while i < len(left):
        my_arr[k] = left[i]
        i = i + 1
        k = k + 1
    
    while j < len(right):
        my_arr[k] = right[j]
        j = j + 1
        k = k + 1
    return total_count

def merge_sort_count(my_arr, start, end):
    count = 0
    if start < end:
        middle = (start + end) // 2
        count = count + merge_sort_count(my_arr, start, middle)
        count = count + merge_sort_count(my_arr, middle + 1, end)
        count = count + merge_and_count(my_arr, start, middle, end)
    return count

size = int(input())
numbers = list(map(int, input().split()))
result = merge_sort_count(numbers, 0, size - 1)
print(result)