def main():
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    print(lis(lst))


def lis(lst):
    a = [-1] + lst
    n = len(lst)
    L = [0] * (n+1)
    P = [-1] * (n+1)
    for i in range(1, n + 1):
        k = 0
        for j in range(i):
            if a[j] < a[i] and L[j] > L[k]:
                k = j
        L[i] = L[k] + 1
        P[i] = k
    return max(L)


if __name__ == '__main__':
    main()
