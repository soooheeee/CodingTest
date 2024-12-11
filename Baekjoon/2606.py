

# import sys

# def input():
#     return sys.stdin.readline().strip()

# def build_graph(edges):
#     graph = {}
#     for u, v in edges:
#         if u not in graph:
#             graph[u] = []
#         graph[u].append(v)
#     return graph

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]

# Building the graph
mygraph = build_graph(edges)

def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph.get(node, []))  # Safely handle nodes without neighbors
    return visited

# Example start node - ensure this is a valid node in your graph
start_node = 1
print(dfs(mygraph, start_node))



# 컴퓨터의 수
v = int(input())
# 네트워크 쌍 개수
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[a].append(b)
    graph[b].append(a)


# 스택 구현
def dfs(x):
    stack = [x]
    visited[x] = True
    count = 0
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
                count += 1
    return count

visited = [False for _ in range(v+1)]
print(dfs(1))