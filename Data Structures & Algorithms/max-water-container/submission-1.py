class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        max = 0

        while lp != rp:
            area = min(heights[lp], heights[rp]) * (rp - lp)
            if area > max:
                max = area
            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -= 1
        return max