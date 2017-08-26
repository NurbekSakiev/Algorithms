def get_shortest_unique_substring(arr, str):
    count = len(arr)
    newArr = [0] * 128
    for i in arr:
        newArr[ord(i)] += 1

    left, right = 0, 0 
    minLen = sys.maxint

    while right < len(str):
        if newArr[ord(str[right])] > 0:
            count -= 1
        newArr[ord(str[right])] -= 1
        while count == 0 and left <= right:
            newArr[ord(str[left])] += 1
            if newArr[ord(str[left])] > 0:
                count += 1
            if right - left + 1 < minLen:
                minLen = right - left + 1
                minStart = left
            left += 1
        right += 1

    return str[minStart : minStart + minLen] if minLen != sys.maxint else ""