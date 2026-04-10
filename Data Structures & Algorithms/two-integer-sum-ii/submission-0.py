class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp = 0
        rp = len(numbers) - 1
        while fp < rp:
            twosome = numbers[fp] + numbers[rp]
            if twosome == target:
                return [fp + 1, rp + 1]
            elif twosome > target:
                rp -= 1
            else:
                fp += 1