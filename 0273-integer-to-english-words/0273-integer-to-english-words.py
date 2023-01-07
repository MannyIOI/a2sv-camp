class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        self.nums = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        
        level = [
            "Thousand",
            "Million",
            "Billion"
        ]
        
        num = str(num)
        temp = []
        numArray = []
        
        for i in range(len(num) - 1, -1, -1):
            temp.append(num[i])
            if len(temp) % 3 == 0:
                number = int(''.join(temp[::-1]))
                numArray.append(self.threeDigitToWord(number))
                temp = []
        
        if temp:
            number = int(''.join(temp[::-1]))
            numArray.append((self.threeDigitToWord(number)))
        
        finalArray = []
        currLevel = len(numArray) - 2
        for i in range(len(numArray)):
            currString = numArray[len(numArray) - 1 - i]
            if len(currString) > 0:
                finalArray.append(currString)
                if currLevel >= 0:
                    finalArray.append(level[currLevel])
            currLevel -= 1
        
        return ' '.join(finalArray).strip()
                
        

    def threeDigitToWord(self, num: int):    
        if num == 0:
            return ""
        twoDigits = num % 100
        hundredDigits = num // 100
        
        ans = []
        if hundredDigits != 0:
            ans.append(self.nums[hundredDigits])
            ans.append("Hundred")
        
        ans += self.upToTwoDigitToWord(twoDigits)
        
        return " ".join(ans)
        
    
    def upToTwoDigitToWord(self, num):
        upToTwenty = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen"
        ]
        
        tens = [
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety"
        ]
        
        if num == 0:
            return []
        
        if num < 10:
            return [self.nums[num]]

        elif num >= 10 and num < 20:
            return [upToTwenty[num - 10]]
        
        else:
            onesDigit = num % 10
            num = num // 10
            tensDigit = num % 10
            num = num // 10
            
            ans = []
            
            ans.append(tens[tensDigit - 2])
            if onesDigit != 0:
                ans.append(self.nums[onesDigit])
            
            return ans
        
        
        