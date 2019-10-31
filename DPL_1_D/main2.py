from bisect import bisect_left


def main():
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    print(lis(lst))


def lis(A: list):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        else:
            L[bisect_left(L, a)] = a
    return len(L)


if __name__ == '__main__':
    main()
