#implementation of A* Search for a weighted graph.
#Problem Statement: Given a weighted graph (e.g., a transportation network with travel
#costs) and a heuristic function, find the minimum-cost path between two nodes.

#code 
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, [start]))

    visited = set()

    while open_list:
        f, current, path = heapq.heappop(open_list)

        if current == goal:
            return f, path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g = f - heuristic[current] + cost
                h = heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (g + h, neighbor, path + [neighbor])
                )

    return float("inf"), []
