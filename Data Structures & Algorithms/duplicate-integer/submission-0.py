from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cntr = Counter()
        for num in nums:
            cntr[num] += 1
        if any(count > 1 for count in cntr.values()):
            return True
        else:
            return False