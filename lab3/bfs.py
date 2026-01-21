from collections import deque

graph = {
    1: [2, 4, 8],
    2: [3],
    3: [],
    4: [8],
    5: [],
    8: [1,3,5]
}
def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.append(node)
            queue.extend(graph[node])
bfs(1)
