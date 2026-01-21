graph = {
    1: [2, 4, 8],
    2: [3],
    3: [],
    4: [8],
    5: [],
    8: [1,3,5]
}

# def dfs(start):
#     visited = []
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node)
#             visited.append(node)
#             stack.extend(reversed(graph[node]))
# dfs(1)


def dfs(start):
    visited=[]
    stack=[start]
    
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node)
            visited.append(node)
            stack.extend(reversed(graph[node]))
dfs(1)