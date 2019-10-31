MAX = 1000


def main():
    n = int(input())
    L = [[0]*(MAX+1) for _ in range(MAX+1)]

    for _ in range(n):
        a = input()
        b = input()

        n, m = len(a), len(b)

        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    L[i+1][j+1] = L[i][j] + 1
                else:
                    L[i+1][j+1] = max(L[i+1][j], L[i][j+1])
        print(L[n][m])


if __name__ == '__main__':
    main()
