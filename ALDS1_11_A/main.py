def main():
    n = int(input())

    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        u, k, *v_s = map(int, input().split(' '))
        for j in range(k):
            graph[u-1][v_s[j-1]-1] = 1

    for row in graph:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
