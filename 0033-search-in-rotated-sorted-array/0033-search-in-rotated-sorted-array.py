class Solution:
    def search(self, A: List[int], target: int) -> int:
        l, r = 0, len(A) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == A[mid]:
                return mid

            if A[mid] >= A[l]:
                if A[l] > target or target > A[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if A[r] < target or target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1