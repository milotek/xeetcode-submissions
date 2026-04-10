class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.upper()
        print(s)
        for x in range(len(s) // 2):
            if s[x].upper() != s[-x-1].upper():
                return False
        return True

            