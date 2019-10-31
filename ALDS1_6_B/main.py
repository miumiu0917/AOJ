def main():
    n = int(input())
    a_s = list(map(int, input().split(' ')))
    q = partition(a_s, 0, n-1)

    def display(index, a):
        if index == q:
            return '[{}]'.format(a)
        else:
            return str(a)

    print(' '.join([display(i, a) for i, a in enumerate(a_s)]))


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


if __name__ == "__main__":
    main()
