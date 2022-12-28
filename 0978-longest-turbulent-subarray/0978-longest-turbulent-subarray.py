class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        maxVal = 0
        sign = 'gt'
        curr = 0
        
        for i in range(len(arr) - 1):
            if sign == 'lt' and arr[i] > arr[i + 1]:
                sign = 'gt'
                curr += 1
            elif sign == 'gt' and arr[i] < arr[i + 1]:
                sign = 'lt'
                curr += 1
            elif arr[i] > arr[i + 1]:
                sign = 'gt'
                curr = 1
            elif arr[i] < arr[i + 1]:
                sign = 'lt'
                curr = 1
            else:
                curr = 0
        
            maxVal = max(maxVal, curr)

        return maxVal + 1
                