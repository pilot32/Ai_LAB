import heapq
from collections import deque

graph_weighted = {
    'S': [('A', 1), ('B', 3), ('C', 5)],
    'A': [('H', 3)],
    'B': [('F', 5)],
    'C': [('E', 2)],
    'E': [('D', 1)]
}

graph_unweighted = {
    'S': ['A','B','C'],
    'A': ['D','M'],
    'B': ['E'],
    'C': ['F'],
    'D': ['H'],
    'E': ['I'],
    'F':[],
    'H': ['G'],
    'I':[],
    'M':[],
    'G':[]
}

def bfs(start):
    visited=[]
    queue=deque([start])
    
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node)
            visited.append(node)
            queue.extend(graph_unweighted[node])
            
bfs('S')            
    
    
def ucs_heap(graph, start, goal):
    frontier = [] 
    heapq.heappush(frontier, (0, start, [start]))
    best_cost = {start: 0}

    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, cost

        if cost > best_cost.get(node, float('inf')):
            continue

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return None, float('inf')

path, cost = ucs_heap(graph_weighted, 'S', 'E')
print("UCS path:", path)
print("UCS cost:", cost)