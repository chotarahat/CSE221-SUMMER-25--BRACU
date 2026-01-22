#Task F. An Ancient Sorting Algorithm
n = int(input())
nums = input().split()
arr = []
for i in range(n):
    arr.append(int(nums[i]))
sorted = True
while sorted:
    sorted = False
    for i in range(n-1):
        if (arr[i] % 2 == arr[i + 1] % 2) and arr[i] > arr[i +1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            sorted = True
for i in range(n):
    print(arr[i], end=" ")
print()