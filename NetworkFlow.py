from collections import deque

MAX_V = 100  # Max number of vertices
INF = float('inf')  # Infinity

def bfs(par, src, snk):
    par[src] = src
    visited = [False] * len(adjList)
    queue = deque([src])

    while queue:
        u = queue.popleft()
        visited[u] = True

        for v in adjList[u]:
            if not visited[v] and cap[u][v] > 0:
                par[v] = u
                queue.append(v)
                if v == snk:
                    return True  # If sink is reached
    return False  # Sink not reached

def fordFulkerson(src, snk):
    maxFlow = 0
    par = [-1] * len(adjList)  # Parent array to store augmenting path

    while bfs(par, src, snk):
        pathFlow = INF
        v = snk
        while v != src:
            u = par[v]
            pathFlow = min(pathFlow, cap[u][v])
            v = par[v]

        v = snk
        while v != src:
            u = par[v]
            cap[u][v] -= pathFlow
            cap[v][u] += pathFlow
            v = par[v]

        maxFlow += pathFlow

    return maxFlow

if __name__ == "__main__":
    instances = int(input())

    for _ in range(instances):
        n, m = map(int, input().split())

        cap = [[0] * n for _ in range(n)]
        adjList = [[] for _ in range(n)]

        for _ in range(m):
            from_node, to_node, capacity = map(int, input().split())
            from_node -= 1
            to_node -= 1

            cap[from_node][to_node] += capacity
            if to_node not in adjList[from_node]:
                adjList[from_node].append(to_node)
                adjList[to_node].append(from_node)

        print(fordFulkerson(0, n - 1))

