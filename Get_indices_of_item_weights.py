def get_indices_of_item_weights(arr, limit):
  dic = {}
  
  for i in range(len(arr)):
    if limit - arr[i] in dic:
      for v in dic[limit - arr[i]]:
        if v != i:
          return [i,v]
    dic[arr[i]] = [i] if arr[i] not in dic else dic[arr[i]] + [i]
  return []