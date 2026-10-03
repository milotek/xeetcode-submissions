class Solution:
    def reverseString(self, s: list[str]) -> None:
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            l = s[lp]
            r = s[rp]
            s[lp] = r
            s[rp] = l
            lp += 1
            rp -= 1