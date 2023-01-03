class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        if len(digits) == 0:
            return []
        
        combinations = []
        
        def backtrack(path, index):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            for letter in mapping[int(digits[index])]:
                path.append(letter)
                backtrack(path, index + 1)
                path.pop()
        
        backtrack([], 0)
        return combinations