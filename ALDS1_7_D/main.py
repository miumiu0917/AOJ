def reconstruction(l, r, pre, _in, result):
    if l >= r:
        return
    c = pre[0]
    del pre[0]
    m = _in.index(c)
    reconstruction(l, m, pre, _in, result)
    reconstruction(m+1, r, pre, _in, result)
    result.append(str(c))


def main():
    n = int(input())
    pre_order = list(map(int, input().split(' ')))
    in_order = list(map(int, input().split(' ')))
    ans = []
    reconstruction(0, n, pre_order, in_order, ans)
    print(' '.join(ans))


if __name__ == '__main__':
    main()
