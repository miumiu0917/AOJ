W_MAX = 10000
K_MAX = 100000


def main():
    n, k = map(int, input().split(' '))
    ws = [int(input()) for _ in range(n)]
    start = 1
    end = n*K_MAX
    target = int((start + end) / 2)
    while end > start:
        if number(target, ws) <= k:
                end = target
        elif number(target, ws) > k:
            start = target + 1
        target = int((start + end) / 2)
    print(target)


def number(p, ws):
    _p = p
    num_track = 1
    for w in ws:
        if w > p:
            return K_MAX+1
        if w > _p:
            _p = p
            num_track += 1
        if w <= _p:
            _p -= w
    return num_track


if __name__ == '__main__':
    main()
