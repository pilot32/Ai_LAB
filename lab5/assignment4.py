#Objective: Implement Uniform Cost Search for a weighted graph.
#Problem Statement: Given a weighted graph (e.g., a transportation network with travel
#costs), find the minimum-cost path between two nodes.

#Tasks:
#● Represent the graph as an adjacency list.
#● Implement Uniform Cost Search to find the optimal path.
#● Compare it with BFS for unweighted graphs.

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
import heapq

def uniform_cost_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        pq,
                        (cost + weight, neighbor, path + [neighbor])
                    )

    return None, float('inf')
start = 'A'
goal = 'D'

ucs_path, ucs_cost = uniform_cost_search(graph, start, goal)
print("UCS Path:", ucs_path)
print("UCS Cost:", ucs_cost)