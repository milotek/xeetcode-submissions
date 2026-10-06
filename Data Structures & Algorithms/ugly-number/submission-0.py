class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for factor in [5, 3, 2]:
            while n % factor == 0:
                n = n / factor
                print(n)

        return n == 1