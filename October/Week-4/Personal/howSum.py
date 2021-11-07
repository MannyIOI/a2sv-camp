def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum].copy()
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        
        if remainderCombination is not None:
            remainderCombination.append(num) 
            if shortestCombination is None or len(remainderCombination) < len(shortestCombination):                
                shortestCombination = remainderCombination
            
    memo[targetSum] = shortestCombination.copy()
    return shortestCombination

print(bestSum(100, [1, 2, 5, 25]))