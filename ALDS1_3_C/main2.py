from collections import deque


def main():
    lst = deque()
    n = int(input())
    for _ in range(n):
        inputs = input().split(' ')
        command = inputs[0]
        if command == 'insert':
            lst.appendleft(inputs[1])
        elif command == 'delete':
            try:
                lst.remove(inputs[1])
            except Exception:
                pass
        elif command == 'deleteFirst':
            lst.popleft()
        elif command == 'deleteLast':
            lst.pop()
    result = ''
    while len(lst) > 0:
        result += lst.popleft() + ' '
    print(result.strip())


if __name__ == '__main__':
    main()