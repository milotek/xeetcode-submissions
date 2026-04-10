import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for x in range(len(nums)):
            calc = 1
            for y in range(len(nums)):
                if y != x:
                    calc *= nums[y]
            output.append(calc)
        return output
            

        # for x in range(len(nums)):
        #     output[x] = math.prod(nums) / nums[x]