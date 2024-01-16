### --- Day 24: Air Duct Spelunking ---

You've finally met your match; the doors that provide access to the roof are locked tight, and all of the controls and related electronics are inaccessible. You simply can't reach them.

The robot that cleans the air ducts, however, **can**.

It's not a very fast little robot, but you reconfigure it to be able to interface with some of the exposed wires that have been routed through the [HVAC](https://en.wikipedia.org/wiki/HVAC) system. If you can direct it to each of those locations, you should be able to bypass the security controls.

You extract the duct layout for this area from some blueprints you acquired and create a map with the relevant locations marked (your puzzle input). 0 is your current location, from which the cleaning robot embarks; the other numbers are (in **no particular order**) the locations the robot needs to visit at least once each. Walls are marked as `#`, and open passages are marked as `.`. Numbers behave like open passages.

For example, suppose you have a map like the following:

```
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
```

To reach all of the points of interest as quickly as possible, you would have the robot take the following path:

 - `0` to `4` (`2` steps)
 - `4` to `1` (`4` steps; it can't move diagonally)
 - `1` to `2` (`6` steps)
 - `2` to `3` (`2` steps)

Since the robot isn't very fast, you need to find it the **shortest route**. This path is the fewest steps (in the above example, a total of `14`) required to start at `0` and then visit every other location at least once.

Given your actual map, and starting from location `0`, what is the fewest number of steps required to visit every non-`0` number marked on the map at least once?

### --- Part 2 ---

Of course, if you leave the cleaning robot somewhere weird, someone is bound to notice.

What is the fewest number of steps required to start at `0`, visit every non-`0` number marked on the map at least once, and then **return to `0`**?

### [--- Solution ---](day-24.py)
```Python
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
```