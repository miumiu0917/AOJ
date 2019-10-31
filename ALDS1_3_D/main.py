from collections import deque


def main():
    sequence = input()
    stack = deque()
    pools = deque()
    for i, e in enumerate(sequence):
        if e == '\\':
            stack.append(i)
        elif e == '_':
            continue
        else:
            if len(stack) == 0:
                continue
            pre = stack.pop()
            s = 0
            while len(pools) > 0 and pre < pools[-1][1]:
                tmp = pools.pop()
                s += tmp[0]
            pools.append((s + i - pre, i))
    length = str(len(pools))
    results = list(map(lambda x: x[0], pools))
    print(sum(results))
    print(' '.join([length] + [str(r) for r in results]))


if __name__ == '__main__':
    main()
