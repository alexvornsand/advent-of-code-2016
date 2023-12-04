### [--- Day 3: Squares With Three Sides ---](https://adventofcode.com/2016/day/3)

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... `5 10 25`? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because `5 + 10` is not larger than `25`.

In your puzzle input, **how many** of the listed triangles are **possible**?

### --- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three **vertically**. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

```
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
```

In your puzzle input, and instead reading by columns, **how many** of the listed triangles are **possible**?

### [--- Solution ---](day-03.py)

```Python
# advent of code 2016
# day 3

import re

file = 'input.txt'

class TriangleSides:
    def __init__(self, triangles):
        self.horizontal_triangles = triangles
        self.vertical_triangles = []
        for r in range(int(len(self.horizontal_triangles) / 3)):
            for c in range(3):
                i = triangles[r * 3 + 0][c]
                j = triangles[r * 3 + 1][c]
                k = triangles[r * 3 + 2][c]
                self.vertical_triangles.append([i, j, k])
        
    def countLegitTriangles(self, triangles):
        legit = 0
        for triangle in triangles:
            a, b, c = triangle
            if a + b > c and a + c > b and b + c > a:
                legit += 1
        return legit

def part_1(triangleSides):
    print('Part 1:', triangleSides.countLegitTriangles(triangleSides.horizontal_triangles))

def part_2(triangleSides):
    print('Part 2:', triangleSides.countLegitTriangles(triangleSides.vertical_triangles))

def main():
    triangles = [[int(side.strip()) for side in list(re.findall('\d+\s?', triangle))] for triangle in open(file, 'r').read().splitlines()]
    triangleSides = TriangleSides(triangles)
    part_1(triangleSides)
    part_2(triangleSides)

if __name__ == '__main__':
    main()
```