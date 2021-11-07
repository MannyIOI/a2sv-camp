import math
def update_files(n, k, updated=1, steps = 0):
    while updated < k:
        updated *= 2
        steps += 1
    ans = (n - updated) % k
    if ans == 0:
        return steps + (n - updated) // k
    return steps + ((n - updated) // k) + 1


testcases = int(input())
for i in range(testcases):
    n, k = map(int, input().split())
    print(update_files(n, k))

