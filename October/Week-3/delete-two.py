from typing import DefaultDict


def delete_two_elements(nums):
    sm = sum(nums)
    x = (2 * sm) / len(nums)
    seen = {}
    # print(x)
    count = 0
    for i in nums:
        if i in seen:
            count += seen[i]
        if x - i in seen:
            seen[x - i] += 1
        else:
            seen[x - i] = 1
    
    return count

number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    n = int(input())
    nums = [int(i) for i in input().split()]

    print(delete_two_elements(nums))