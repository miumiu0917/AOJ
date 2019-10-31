

def main():
    n = int(input())
    rs = [int(input()) for _ in range(n)]
    result = -2000000000000
    history_min = rs[0]
    for r in rs[1:]:
        result = max(result, r - history_min)
        history_min = min(history_min, r)
    print(result)
        


if __name__ == '__main__':
    main()