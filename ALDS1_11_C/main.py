from collections import deque

N = 100
n = 0
M = None
WHITE = 0
GRAY = 1
BLACK = 2
INF = float('inf')
d = None


def main():
    global n, M, d
    M = [[0 for _ in range(N)] for _ in range(N)]
    n = int(input())
    d = [INF for _ in range(n)]

    for _ in range(n):
        u, k, *v_s = map(int, input().split(' '))
        for j in range(k):
            M[u-1][v_s[j-1]-1] = 1

    bfs()

    for i in range(n):
        print('{} {}'.format(i+1, d[i] if d[i] != INF else -1))


def bfs():
    q = deque()
    q.appendleft(0)
    d[0] = 0

    while len(q) > 0:
        u = q.pop()
        for v in range(n):
            if M[u][v] == WHITE:
                continue
            if d[v] != INF:
                continue
            d[v] = GRAY
            d[v] = d[u] + 1
            q.appendleft(v)


if __name__ == '__main__':
    main()
