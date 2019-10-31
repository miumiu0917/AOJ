from functools import reduce
import math

orientation = math.cos(math.pi/3) + 1j * math.sin(math.pi/3)


def main():
    n = int(input())
    results = [(0.0, 0.0), (100.0, 0.0)]
    results = koch_curve(results, 0, n)
    for r in results:
        print(r[0], r[1])


def f(a, b):
    c = ((2*a[0]+b[0])/3, (2*a[1]+b[1])/3)
    d = ((a[0]+2*b[0])/3, (a[1]+2*b[1])/3)
    vec = d[0] + d[1]*1j - (c[0] + 1j*c[1])
    e = vec * orientation
    e += (c[0] + 1j*c[1])
    e = (e.real, e.imag)
    return [a, c, e, d]


def koch_curve(lst, i, maximum):
    if i == maximum:
        return lst
    else:
        results = []
        l = len(lst)
        for j in range(l-1):
            results += f(lst[j], lst[j+1])
        results += [lst[j+1]]
        return koch_curve(results, i+1, maximum)


if __name__ == '__main__':
    main()
