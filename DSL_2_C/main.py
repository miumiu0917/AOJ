import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


class Node:

    def __init__(self, location=None, p=None, l=None, r=None):
        self.location = location
        self.p = p
        self.l = l
        self.r = r


class Point:

    def __init__(self, _id, x, y):
        self.id = _id
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return str(self.id)


MAX = 1000000
P = [None for _ in range(MAX)]
T = [Node() for _ in range(MAX)]
np = 0


def lessX(p1, p2):
    return p1.x < p2.x


def lessY(p1, p2):
    return p1.y < p2.y


def makeKDTree(l, r, depth):
    global np
    if not l < r:
        return -1

    mid = int((l + r) // 2)
    t = np
    np += 1

    if depth % 2 == 0:
        P[l:r] = sorted(P[l:r], key=lambda p: p.x)
    else:
        P[l:r] = sorted(P[l:r], key=lambda p: p.y)

    T[t].location = mid
    T[t].l = makeKDTree(l, mid, depth+1)
    T[t].r = makeKDTree(mid+1, r, depth+1)

    return t


def find(v, sx, tx, sy, ty, depth, ans):
    x = P[T[v].location].x
    y = P[T[v].location].y

    if sx <= x and x <= tx and sy <= y and y <= ty:
        ans.append(P[T[v].location])

    if depth % 2 == 0:
        if T[v].l != -1:
            if sx <= x:
                find(T[v].l, sx, tx, sy, ty, depth+1, ans)
        if T[v].r != -1:
            if x <= tx:
                find(T[v].r, sx, tx, sy, ty, depth+1, ans)
    else:
        if T[v].l != -1:
            if sy <= y:
                find(T[v].l, sx, tx, sy, ty, depth+1, ans)
        if T[v].r != -1:
            if y <= ty:
                find(T[v].r, sx, tx, sy, ty, depth+1, ans)


def main():
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split(' '))
        P[i] = Point(i, x, y)

    root = makeKDTree(0, n, 0)

    q = int(input())

    for _ in range(q):
        sx, tx, sy, ty = map(int, input().split(' '))
        ans = []
        find(root, sx, tx, sy, ty, 0, ans)
        if ans:
            print('\n'.join(map(str, sorted(ans, key=lambda p: p.id))))
        print()


if __name__ == '__main__':
    main()
