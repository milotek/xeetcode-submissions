class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nice = defaultdict(list)
        for x in strs:
            sortedS = ''.join(sorted(x))
            nice[sortedS].append(x)
        return list(nice.values())
                    
                    