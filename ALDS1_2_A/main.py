def main():
    n = int(input())
    array = [int(i) for i in input().split(' ')]

    count = 0
    for i in range(n):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                count += 1
                array[j], array[j-1] = array[j-1], array[j]
    print(' '.join(map(str, array)))
    print(count)


if __name__ == '__main__':
    main()
