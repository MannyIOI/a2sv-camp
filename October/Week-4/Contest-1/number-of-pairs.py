def number_of_pairs(list, left, right):
    i1, i2, j = 0, 0, len(list) - 1
    ans = 0
    while j > 0 and i2 < j and i1 < j:
        print(i1, i2, j, ans)
        if list[j] + list[i1] < left and list[j] + list[i2] < left:
            i1 += 1
            i2 += 1
        elif list[j] + list[i2] > right:
            j -= 1
            i2 = i1
        elif list[j] + list[i1] < left:
            i1 += 1
        elif list[j] + list[i2] < right:
            i2 += 1
            ans += 1
        elif list[j] + list[i2] <= right and list[j] + list[i1] >= left:
            # ans += i2 - i1 + 1
            j -= 1
            i2 = i1

    return ans

testcases = int(input())

for i in range(testcases):
    size, left, right = [int(i) for i in input().split()]
    list = [int(i) for i in input().split()]

    ans = number_of_pairs(sorted(list), left, right)
    print(ans)