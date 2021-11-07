import heapq
def connections(inputs):
    store = {}
    for index in range(len(inputs)):
        if inputs[index] in store:
            store[inputs[index]].append(index)
        else:
            store[inputs[index]]=[index]
    heap = []
    for each in store:
        heapq.heappush(heap,(len(store[each]),store[each]))
    print(heap)
    while heap:
        
n = list(map(int,input().split()))
#for i in range(n):
print(connections(n))