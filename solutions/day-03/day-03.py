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