INF = float('inf')


def main():
    n = int(input())
    p = [0 for _ in range(n+1)]

    for i in range(n):
        p1, p2 = map(int, input().split(' '))
        p[i-1], p[i] = p1, p2

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = INF
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j])
    print(dp[1][n])


if __name__ == "__main__":
    main()
