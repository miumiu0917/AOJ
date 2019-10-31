
def main():
    n = int(input())

    pre = 1
    cur = 1

    for _ in range(n-1):
        tmp = cur
        cur = pre + cur
        pre = tmp

    print(cur)


if __name__ == '__main__':
    main()
