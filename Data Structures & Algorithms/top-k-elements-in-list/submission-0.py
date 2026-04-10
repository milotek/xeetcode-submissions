from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        mc = c.most_common(k)
        mck = [x[0] for x in mc]
        return(mck)
        