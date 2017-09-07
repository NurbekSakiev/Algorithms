def find_array_quadruplet(arr, s):
  d = {}
  
  for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
      currSum = arr[i] + arr[j]
      res = [i,j]
      
      if s - currSum in d:
        for k in range(len(d[s - currSum])):
          if d[s - currSum][k] not in res:
            res.append(d[s - currSum][k])
            if len(res) == 4:
              res = map(lambda x: arr[x], res)
              return sorted(res)
      d[currSum] = [i,j] if currSum not in d else d[currSum] + [i,j]
     
  return []

#Solution 2

def find_array_quadruplet(arr, s):
  arr.sort()
  for i in range(len(arr) - 3):
    first = arr[i]; last = arr[-1]
    start, end = i + 1, len(arr) - 2
    
    while start < end:
      currSum = first + last + arr[start] + arr[end]
      if currSum == s:
        return [first,arr[start],arr[end], last]
      elif currSum < s:
        start += 1
      else:
        end -= 1
  return []
  