

def main():
    n = int(input())
    array = [int(i) for i in input().split(' ')]
    my_print(array)
    for i in range(1, n):
        target = array[i]

        j = i - 1
        while target < array[j] and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = target
        my_print(array)


def my_print(array):
    print(' '.join(map(str, array)))


if __name__ == '__main__':
    main()
