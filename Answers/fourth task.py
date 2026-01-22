#Task D. Is Sorted?
def non_decreasing(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
      return False
  return True

a = int(input())
for i in range(a):
  N = int(input())
  elem = input()
  numbers = elem.split()
  arr = []
  for i in range(N):
    arr.append(int(numbers[i]))
  if non_decreasing(arr):
    print("YES")
  else:
    print("NO")