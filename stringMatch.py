def stringMatch(t, p):
	m = len(p)
	n = len(t)
	for i in range(n-m):
    		j = 0
    		while j < m and t[i+j] == p[j]:
      			j += 1
    		if j == m: return i
  
	return -1
