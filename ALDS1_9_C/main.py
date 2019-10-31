MAX = 2000000
H = 0
INF = float('inf')


def parent(i):
    return i//2


def left(i):
    return 2*i


def right(i):
    return 2*i+1


def max_heapify(A, i):
    l = left(i)
    r = right(i)

    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= H and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(H//2, 0, -1):
        max_heapify(A, i)


def insert(A, v):
    global H
    H += 1
    A[H] = -1*INF
    heap_increase_key(A, v)


def heap_increase_key(A, v):
    i = H
    if v < A[i]:
        raise ValueError('err')
    A[i] = v
    while i > 1 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def heap_extract_max(A):
    global H
    if H < 1:
        raise ValueError('err')
    _max = A[1]
    A[1] = A[H]
    H -= 1
    max_heapify(A, 1)
    return _max


def main():
    global H
    A = [0] * (MAX+1)

    _in = input().split(' ')

    while _in[0] != 'end':

        if _in[0] == 'insert':
            v = int(_in[1])
            insert(A, v)
        else:
            v = heap_extract_max(A)
            print(v)

        _in = input().split(' ')


if __name__ == '__main__':
    main()
