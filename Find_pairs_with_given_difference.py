 def find_pairs_with_given_difference(arr, k):
        arr.sort()
      
        res = []
          
        start = 0; end = 1
          
        while end < len(arr) and start < end:
            if arr[end] - arr[start] == k:
                res.append([arr[start], arr[end]])
            elif arr[end] - arr[start] < k:
                end += 1
            else:
                start += 1
        return res

# Solution 2

    def find_pairs_with_given_difference(arr, k):
        arr.sort()
      
        res = []
      
        for i in range(len(arr)):
            toSearch = arr[i] + k
            start, end = i + 1, len(arr) - 1
            while start < end:
                mid = (start + end) // 2
                if arr[mid] == toSearch:
                    res.append([arr[mid], arr[i]])
                elif arr[mid] < toSearch:
                    start = mid + 1
                else:
                    end = mid - 1
        return res