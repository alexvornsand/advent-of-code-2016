# advent of code 2016
# day 24

from functools import cache
from collections import defaultdict

file = 'input.txt'

class Maze:
    def __init__(self, grid):
        self.map = {(c, r): grid[r][c] for r in range(len(grid)) for c in range(len(grid[r]))}
        self.points_of_interest = {value: key for key, value in self.map.items() if self.map[key].isdigit()}

    def findPath(self, a, b):
        navigable_tiles = [key for key in self.map if self.map[key] != '#']
        visited_nodes = []
        distances = defaultdict(lambda: 999999)
        distances[a] = 0
        queue = [a]
        while queue:
            x, y = queue.pop(0)
            if (x, y) == b:
                return distances[b]
            else:
                visited_nodes.append((x, y))
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1,0 )]:
                    if (x + dx, y + dy) in navigable_tiles and (x + dx, y + dy) not in visited_nodes:
                        distances[(x + dx, y + dy)] = min(distances[(x, y)] + 1, distances[(x + dx, y + dy)])
                        if (x + dx, y + dy) not in queue:
                            queue.append((x + dx, y + dy))

    def findPaths(self):
        self.path_lengths = {}
        for i in self.points_of_interest:
            for j in self.points_of_interest:
                if int(j) > int(i):
                    self.path_lengths[(i, j)] = self.findPath(self.points_of_interest[i], self.points_of_interest[j])
                    self.path_lengths[(j, i)] = self.path_lengths[(i, j)]

    @cache
    def navigateMaze(self, position, unvisited, return_trip=False):
        if len(unvisited) == 0:
            return self.path_lengths[(position, '0')] if return_trip else 0
        else:
            return min([self.path_lengths[(position, node)] + self.navigateMaze(node, tuple([x for x in unvisited if x != node]), return_trip) for node in unvisited])

def part_1(maze):
    print('Part 1:', maze.navigateMaze('0', tuple([x for x in maze.points_of_interest if x != '0'])))

def part_2(maze):
    print('Part 2:', maze.navigateMaze('0', tuple([x for x in maze.points_of_interest if x != '0']), True))

def main():
    grid = [[x for x in row] for row in open(file, 'r').read().splitlines()]
    maze = Maze(grid)
    maze.findPaths()
    part_1(maze)
    part_2(maze)

if __name__ == '__main__':
    main()