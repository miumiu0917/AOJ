N = 100
INF = float('inf')
M = [[INF for _ in range(N)] for _ in range(N)]
n = 0
WHITE = 0
GRAY = 1
BLACK = 2
color = [WHITE for _ in range(N)]
d = [INF for _ in range(N)]
p = [0 for _ in range(N)]


def main():
    global N
    n = int(input())
    for i in range(n):
        a_s = list(map(int, input().split(' ')[1:]))
        for j in range(n):
            if a_s[j] != -1:
                M[i][j] = M[j][i] = a_s[j]
    print(prim(n))


def prim(n):
    d[0] = 0
    p[0] = -1

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
            if color[v] != BLACK and M[u][v] < INF:
                if M[u][v] < d[v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = GRAY
    return sum(d[:n])


if __name__ == '__main__':
    main()
