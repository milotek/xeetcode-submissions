class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for x in range(len(arr)-1):
            arr[x] = max(arr[x+1:])
        arr[-1] = -1
        return arr