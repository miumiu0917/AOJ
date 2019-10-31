from collections import deque


def main():
    n, q = map(int, input().split(' '))
    inputs = [input().split(' ') for _ in range(n)]
    inputs = [(p[0], int(p[1])) for p in inputs]
    queue = deque(inputs)
    t = 0
    while len(queue) > 0:
        p = queue.popleft()
        if p[1] > q:
            t += q
            queue.append((p[0], p[1]-q))
        else:
            t += p[1]
            print('{} {}'.format(p[0], t))


if __name__ == '__main__':
    main()
