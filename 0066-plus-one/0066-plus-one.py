class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        curr = len(digits) - 1

        while carry == 1 and curr >= 0:
            if digits[curr] != 9:
                carry = 0

            digits[curr] = (digits[curr] + 1) % 10
            curr -= 1

        if curr == -1 and carry == 1:
            digits = [1] + digits
            
        return digits