from collections import defaultdict, deque

def maxChain(graph):
    visited = set()
    queue = deque()
    queue.append(('polycarp', 1))
    max_chain = 1
    while queue:
        person, level = queue.popleft()
        visited.add((person, level))
        max_chain = max(level, max_chain)

        for i in graph[person]:
            if i not in visited:
                queue.append((i, level + 1))
        
    return max_chain


num_of_connections = int(input())
graph = defaultdict(lambda: [])

for edge in range(num_of_connections):
    dest, _, origin = [i.lower() for i in input().split()]
    graph[origin].append(dest)

print(maxChain(graph))