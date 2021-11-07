n, m = [int(i) for i in input().split()]
listens = [0]
for i in range(n):
    count, time = [int(i) for i in input().split()]
    listens.append(listens[-1] + count * time)

moments = [int(i) for i in input().split()]
j = 1
for i in moments:
    while listens[j] < i:
        j += 1
    print(j)