import heapq

def network_delay_time(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
    
 
    min_heap = [(0, k)]  # (time, node)
    

    shortest_time = {i: float('inf') for i in range(1, n + 1)}
    shortest_time[k] = 0
    
    while min_heap:
        current_time, u = heapq.heappop(min_heap)

        if current_time > shortest_time[u]:
            continue
        
        for v, w in graph[u]:
            time = current_time + w
            if time < shortest_time[v]:
                shortest_time[v] = time
                heapq.heappush(min_heap, (time, v))
    
    max_time = max(shortest_time.values())
    
    return max_time if max_time != float('inf') else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(network_delay_time(times, n, k))
