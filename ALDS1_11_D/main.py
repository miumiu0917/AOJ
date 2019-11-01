from collections import deque


n = 0
m = 0
M = None
color = None


def main():
    global n, m, M, color
    n, m = map(int, input().split(' '))

    M = [[] for _ in range(n)]
    color = [-1 for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split(' '))
        M[a].append(b)
        M[b].append(a)

    num = 1
    for u in range(n):
        if color[u] == -1:
            dfs(u, num)
            num += 1

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split(' '))
        if color[a] == color[b]:
            print('yes')
        else:
            print('no')


def dfs(r, c):
    stack = deque()
    stack.append(r)
    color[r] = c
    while len(stack) > 0:
        u = stack.pop()
        for i in range(len(M[u])):
            v = M[u][i]
            if color[v] == -1:
                color[v] = c
                stack.append(v)


if __name__ == '__main__':
    main()
