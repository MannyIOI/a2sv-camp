def countdown(n, time):
    ls = [int(i) for i in time]
    ans = 0
    for i in range(n - 1, -1, -1):
        if time[i] != '0':
            if i == n - 1:
                ans += int(time[i])
            else:
                ans += int(time[i]) + 1

    return ans
            


test_cases = int(input())

for i in range(test_cases):
    size, clock = int(input()), input()
    print(countdown(size, clock))