def main():
    n = int(input())
    ns = list(map(int, input().split(' ')))
    _ = int(input())
    qs = list(map(int, input().split(' ')))
    count = 0
    for q in qs:
        for n in ns:
            if n == q:
                count += 1
                break
    print(count)


if __name__ == '__main__':
    main()
