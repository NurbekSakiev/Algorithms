def index_equals_value_search(arr):
  start = 0; end = len(arr) - 1
  
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == mid:
      return mid
    elif arr[mid] > mid:
      end = mid - 1
    else:
      start = mid + 1
  return -1