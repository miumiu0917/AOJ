
def main():
    n = int(input())
    A = list(map(int, input().split(' ')))
    q = int(input())
    ms = list(map(int, input().split(' ')))
    results = _enumerate(A)

    for m in ms:
        if m in results:
            print('yes')
        else:
            print('no')


def _enumerate(lst):
    result = [0]
    for e in lst:
        n = len(result)
        for i in range(n):
            result.append(result[i]+e)
    return list(set(result))


if __name__ == '__main__':
    main()
