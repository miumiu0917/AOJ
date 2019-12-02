package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
	"sort"
)

// Point struct.
type Point struct {
	id int
	x int
	y int
}

// Node struct
type Node struct {
	location int
	l int
	r int
}

// MAX : constant value
const MAX = 1000000
var np = 0
// P : array of Point
var P [MAX]*Point
// T : array of Node
var T[MAX]*Node

func find(v int, sx int, tx int, sy int, ty int, depth int, ans []*Point) []*Point {
	x := P[T[v].location].x
	y := P[T[v].location].y

	if sx <= x && x <= tx && sy <= y && y <= ty {
		ans = append(ans, P[T[v].location])
	}

	if depth % 2 == 0 {
		if T[v].l != -1 {
      if sx <= x {
        ans = find(T[v].l, sx, tx, sy, ty, depth+1, ans)
      }
    }
    if T[v].r != -1 {
      if x <= tx {
        ans = find(T[v].r, sx, tx, sy, ty, depth+1, ans)
      }
    }
	} else {
		if T[v].l != -1 {
      if sy <= y {
        ans = find(T[v].l, sx, tx, sy, ty, depth+1, ans)
      }
    }
    if T[v].r != -1 {
      if y <= ty {
        ans = find(T[v].r, sx, tx, sy, ty, depth+1, ans)
      }
    }
	}
	return ans
}

func makeKDTree(l int, r int, depth int) int {
	if !(l < r) {
		return -1
	}

	mid := (l + r) / 2
	t := np
	np++

	if depth % 2 == 0 {
		sort.Slice(P[l:r], func(i int, j int) bool {
			return P[l+i].x < P[l+j].x
		})
	} else {
		sort.Slice(P[l:r], func(i int, j int) bool {
			return P[l+i].y < P[l+j].y
		})
	}

	node := Node {
		location: mid,
		l: makeKDTree(l, mid, depth+1),
		r: makeKDTree(mid+1, r, depth+1),
	}
	T[t] = &node

	return t
}


func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		scanner.Scan()
		xy := strings.Split(scanner.Text(), " ")
		x, _ := strconv.Atoi(xy[0])
		y, _ := strconv.Atoi(xy[1])
		P[i] = &Point{id: i, x: x, y: y}
	}

	root := makeKDTree(0, n, 0)

	scanner.Scan()
	q, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < q; i++ {
		scanner.Scan()
		vs := strings.Split(scanner.Text(), " ")
		sx, _ := strconv.Atoi(vs[0])
		tx, _ := strconv.Atoi(vs[1])
		sy, _ := strconv.Atoi(vs[2])
		ty, _ := strconv.Atoi(vs[3])
		var ans []*Point

		find(root, sx, tx, sy, ty, 0, ans)

		fmt.Println(ans)

		if 0 < len(ans) {
			sort.Slice(ans, func(i int, j int) bool {
				return ans[i].id < ans[j].id
			})
			for _, p := range(ans) {
				fmt.Println(p.id)
			}
		}
		fmt.Println("")
	}
}