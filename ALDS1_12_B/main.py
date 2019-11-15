N = 100
WHITE = 0
GRAY = 1
BLACK = 2
INF = float('inf')
M = None
d = [INF for _ in range(N)]
p = [0 for _ in range(N)]
color = [WHITE for _ in range(N)]
n = 0


def main():
    global n, M

    n = int(input())
    M = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        _, k, *v_s = map(int, input().split(' '))
        for j in range(k):
            c_i = 2*j + 1
            v = v_s[2*j]
            M[i][v] = M[v][i] = v_s[c_i]

    dijkstra(0)

    for i in range(n):
        print('{} {}'.format(i, d[i]))


def dijkstra(s):
    d[s] = 0
    p[s] = -1

    while True:
        mincost = INF
        for i in range(n):
            if color[i] != BLACK and d[i] < mincost:
                mincost = d[i]
                u = i

        if mincost == INF:
            break

        color[u] = BLACK

        for v in range(n):
            if color[v] != BLACK and M[u][v] != INF:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    p[v] = u
                    color[v] = GRAY


if __name__ == '__main__':
    main()
