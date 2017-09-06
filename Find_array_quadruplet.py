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
  