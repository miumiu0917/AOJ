import java.util.Arrays;

data class Point(
  val id: Int,
  val x: Int, 
  val y: Int
)

data class Node(
  var location: Int = 0,
  var p: Int = 0,
  var l: Int = 0,
  var r: Int = 0
)

val MAX = 1000000
var np = 0

val P: Array<Point?> = arrayOfNulls(MAX)
val T: Array<Node> = Array(MAX) { _ -> Node() }

fun makeKDTree(l: Int, r: Int, depth: Int): Int {
  if (!(l < r)) {
    return -1
  }

  val mid = (l + r) / 2
  val t = np
  np++

  if (depth % 2 == 0) {
    Arrays.sort(P, l, r, compareBy { it!!.x })
    // P.sortWith(compareBy { it!!.x }, l, r)  
  } else {
    Arrays.sort(P, l, r, compareBy { it!!.y })
    // P.sortWith(compareBy { it!!.y }, l, r)  
  }

  T[t].location = mid
  T[t].l = makeKDTree(l, mid, depth+1)
  T[t].r = makeKDTree(mid+1, r, depth+1)

  return t
}

fun find(v: Int, sx: Int, tx: Int, sy: Int, ty: Int, depth: Int, ans: MutableList<Point>) {
  val x = P[T[v].location]!!.x
  val y = P[T[v].location]!!.y

  if (sx <= x && x <= tx && sy <= y && y <= ty) {
    ans.add(P[T[v].location]!!)
  }

  if (depth % 2 == 0) {
    if (T[v].l != -1) {
      if (sx <= x) {
        find(T[v].l, sx, tx, sy, ty, depth+1, ans)
      }
    }
    if (T[v].r != -1) {
      if (x <= tx) {
        find(T[v].r, sx, tx, sy, ty, depth+1, ans)
      }
    }
  } else {
    if (T[v].l != -1) {
      if (sy <= y) {
        find(T[v].l, sx, tx, sy, ty, depth+1, ans)
      }
    }
    if (T[v].r != -1) {
      if (y <= ty) {
        find(T[v].r, sx, tx, sy, ty, depth+1, ans)
      }
    }
  }
}

fun main(args: Array<String>) {
  val start = System.currentTimeMillis()

  val n = Integer.parseInt(readLine())
  
  for (i in 0..(n-1)) {
    val (x, y) = readLine()!!.split(" ").map(Integer::parseInt)
    P[i] = Point(i, x, y)
  }
  println(System.currentTimeMillis() - start)
  val root = makeKDTree(0, n, 0)
  println(System.currentTimeMillis() - start)

  val q = Integer.parseInt(readLine())
  
  for (i in 1..q) {
    val (sx, tx, sy, ty) = readLine()!!.split(" ").map(Integer::parseInt)
    val ans = mutableListOf<Point>()
    find(root, sx, tx, sy, ty, 0, ans)
    if (!ans.isEmpty()) {
      val buffer = StringBuilder()
      ans.sortedBy { it.id } .map { it.id.toString() } .joinTo(buffer, separator = "\n")
      println(buffer.toString())
    }
    println()
  }
  println(System.currentTimeMillis() - start)
}