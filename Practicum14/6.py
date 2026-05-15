import heapq


def dijkstra(graph, start, end):
    dist = {start: 0}
    queue = [(0, start)]

    while queue:
        d, u = heapq.heappop(queue)

        if u == end:
            return d

        for v, w in graph.get(u, []):
            if d + w < dist.get(v, float('inf')):
                dist[v] = d + w
                heapq.heappush(queue, (dist[v], v))

    return -1


n, m = int(input()), int(input())

graph = {}
for _ in range(m):
    a, b, d = input().split()
    graph.setdefault(a, []).append((b, int(d)))
    graph.setdefault(b, []).append((a, int(d)))

print(dijkstra(graph, *input().split()))