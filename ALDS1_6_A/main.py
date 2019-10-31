k = 10000


def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    B = [-1] * n

    counting_sort(A, B, n, k)
    print(' '.join(map(str, B)))


def counting_sort(A, B, n, k):
    C = [0] * k

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1


if __name__ == '__main__':
    main()
