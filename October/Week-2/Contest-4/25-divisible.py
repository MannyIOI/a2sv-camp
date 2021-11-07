from itertools import chain, combinations

def powerset(iterable):
    x = len(iterable)
    ans = []
    for i in range(1 << x):
        ans.append([iterable[j] for j in range(x) if (i & (1 << j))])
    return ans

def divisible25(curr):
    n = str(curr)
    divs = ["00","25","50","75"]
    l = len(n)
 
    ans = float('inf')
    for i in range(l):
        for j in range(i + 1,l):            
            if n[i] + n[j] in divs:
                # print(n[i] + n[j])
                delete = j - i - 1 + (l - j - 1)
                ans = min(ans,delete)

    return ans
n = int(input())
for i in range(n):
    print(divisible25(input()))

# print(divisible25('71345'))
# print(divisible25('50555'))
# print(divisible25('501110'))