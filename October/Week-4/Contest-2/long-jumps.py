arr = [5, 3, 1, 2, 3]
def longJumps(arr):
    maximum = float('-inf')
    ans = []

    for i in range(len(arr) - 1, -1, -1):
        item = arr[i]
        # print(ans)
        if item > len(ans):
            # out of range
            ans.append(item)
            maximum = max(item, maximum)
        else:
            new_item = item + ans[len(ans) - item]
            ans.append(new_item)
            maximum = max(maximum, new_item)
    
    
    return maximum
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    print(longJumps(arr))