import heapq

MAX = 10000
WHITE = 0
GRAY = 1
BLACK = 2
INF = float('inf')
color = [WHITE for _ in range(MAX)]
d = [INF for _ in range(MAX)]
adj = [None for _ in range(MAX)]
n = 0


def main():
    global n
    n = int(input())

    for _ in range(n):
        u, k, *n_s = map(int, input().split(' '))
        adj[u] = ([(n_s[2*j], n_s[2*j+1]) for j in range(k)])

    dijkstra(0)

    for i in range(n):
        print(f'{i} {d[i] if d[i] != INF else -1}')


def dijkstra(s):
    d[s] = 0

    pq = []

    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        f = heapq.heappop(pq)
        u = f[1]

        color[u] = BLACK
        if d[u] < f[0]:
            continue

        for j in range(len(adj[u])):
            v = adj[u][j][0]
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + adj[u][j][1]:
                d[v] = d[u] + adj[u][j][1]
                heapq.heappush(pq, (d[v], v))
                color[v] = GRAY


if __name__ == '__main__':
    main()
