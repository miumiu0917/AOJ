from collections import deque


def main():
    sequence = [e for e in input().split(' ')]
    stack = deque()
    for e in sequence:
        if '+' == e:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif '-' == e:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif '*' == e:
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        else:
            stack.append(int(e))
    print(stack.pop())


if __name__ == '__main__':
    main()
