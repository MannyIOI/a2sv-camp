def canReach(total, dest, connections):
    i = 1
    while i < total:
        i += connections[i - 1]
        if i == dest:
            return True
    
    return False

total, dest = [int(i) for i in input().split(' ')]
connections = [int(i) for i in input().split(' ')]

x = canReach(total, dest, connections)
if x:
    print('YES')
else:
    print('NO')
# print(x)