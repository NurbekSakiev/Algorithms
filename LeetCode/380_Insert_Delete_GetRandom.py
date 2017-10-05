class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}; self.nums = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val not in self.dic:
            self.nums.append(val)
            self.dic[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            lastOne = self.nums[-1]; idx = self.dic[val]
            self.nums[idx] = lastOne; self.dic[lastOne] = idx
            self.nums.pop(); self.dic.pop(val, 0)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]