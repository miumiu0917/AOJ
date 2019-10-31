MAX = 1000
VMAX = 10000


def main():
    n = int(input())
    
    a_s = list(map(int, input().split(' ')))
    minimum = min(a_s)

    ans = 0

    t_s = [0] * (VMAX+1)
    b_s = [a for a in a_s]
    v_s = [False for _ in range(n)]
    b_s = sorted(b_s)

    for i in range(n):
        t_s[b_s[i]] = i

    for i in range(n):
        if v_s[i]:
            continue
        cur = i
        S = 0
        m = VMAX
        a_n = 0

        while True:
            v_s[cur] = True
            a_n += 1
            v = a_s[cur]
            m = min(m, v)
            S += v
            cur = t_s[v]
            if v_s[cur]:
                break
        ans += min(S + (a_n-2)*m, m+S+(a_n+1)*minimum)
    
    print(ans)


if __name__ == '__main__':
    main()
