def num_of_paths_to_dest(n):
  matrix = [[0 for i in range(n)] for j in range(n)]
  
  prevCol = [1 for i in range(n)]
  
  
  for i in range(1, n):
    currCol = [0 for k in range(n)]
    for j in range(n):
      if i > j:
        continue
      currCol[j] = currCol[j-1] + prevCol[j]
    prevCol = currCol
    
  return prevCol[n-1]