
def main():
    n = int(input())
    ns = list(map(int, input().split(' ')))
    _ = int(input())
    qs = list(map(int, input().split(' ')))
    count = 0
    start = 0
    end = n
    target = int((start + end) / 2)
    for q in qs:
        while end > start:
            if ns[target] > q:
                end = target
            elif ns[target] < q:
                start = target + 1
            else:
                count += 1
                break
            target = int((start + end) / 2)
        start = 0
        end = n
        target = int((start + end) / 2)
    print(count)


if __name__ == '__main__':
    main()
