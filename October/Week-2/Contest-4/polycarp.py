def polycarp(input):
    consecutive_v_count = 0
    w_count = input.count('w')
    ans = w_count

    for i in range(len(input)):
        if input[i] == 'v':
            consecutive_v_count += 1
        else:
            ans += consecutive_v_count // 2
            consecutive_v_count = 0
    if consecutive_v_count > 0:
        ans += consecutive_v_count // 2
    return ans

n = int(input())
for i in range(n):
    print(polycarp(input()))