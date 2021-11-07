n, k = [int(i) for i in input().split()]

def football(n, k):
    visited = set()
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and (i, j) not in visited and (j, i) not in visited:
                visited.add((i, j))
                count += 1
            if count == k:
                break
        if count != k:
            return False
    return visited

ans = football(n, k)

if not ans:
    print(-1)
else:
    print(len(ans))
    for (i, j) in ans:
        print(f'{i + 1} {j + 1}')