def reverse_words(arr):
  reverse(arr, 0, len(arr) - 1)
  
  start = 0; end = 0;
  while end < len(arr):
    while end < len(arr) and arr[end] != ' ':
      end += 1
    reverse(arr, start, end - 1)
    while end < len(arr) and arr[end] == ' ':
      end += 1
    start = end
    
  return arr
  
def reverse(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1