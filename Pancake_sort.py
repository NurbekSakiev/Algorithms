def flip(arr, k):
  start = 0; end = k - 1;
  
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
  


def pancake_sort(arr):
  until  = len(arr)
  
  for j in range(len(arr)):
    
    biggest = float("-inf")
    biggestIdx = -1
    for i in range(until):
      if arr[i] > biggest:
        biggest = arr[i]
        biggestIdx = i
    flip(arr, biggestIdx + 1)
    flip(arr, until)
    until -= 1
    
  return arr