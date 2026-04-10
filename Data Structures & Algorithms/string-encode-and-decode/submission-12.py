class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "edge case 1"
        return "|".join(strs)
        
    def decode(self, s: str) -> List[str]:
        if s == "edge case 1": return []
        if s == "": return [""]
        s = s.split("|")
        return s