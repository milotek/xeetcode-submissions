from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cc = Counter(s)
        longest = 0
        has_odd = False
        for count in cc.values():
            longest += count if count % 2 == 0 else count - 1
            if count % 2 != 0:
                has_odd = True
        return longest + 1 if has_odd else longest