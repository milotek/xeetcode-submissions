class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        c = Counter(s1)
        c2 = Counter(s2[:len(s1)])

        if c == c2:
            return True

        start = 0
        end = len(s1) - 1
        
        while end < len(s2) - 1:
            if c2[s2[start]] > 1:
                c2[s2[start]] -= 1
            else:
                 del c2[s2[start]]

            start += 1
            end += 1

            c2[s2[end]] += 1

            if c == c2:
                return True
        return False




            
            