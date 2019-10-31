def main():
    n = int(input())
    array = [int(i) for i in input().split(' ')]

    count = 0
    for i in range(n):
        min_i = i
        for j in range(i, n):
            if array[j] < array[min_i]:
                min_i = j
        if min_i != i:
            count += 1
        array[i], array[min_i] = array[min_i], array[i]
    print(' '.join(map(str, array)))
    print(count)


if __name__ == '__main__':
    main()
