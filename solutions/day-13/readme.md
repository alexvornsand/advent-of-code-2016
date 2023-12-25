### [--- Day 13: A Maze of Twisty Little Cubicles ---](https://adventofcode.com/2016/day/13)

You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers `(x,y)`. Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at `0,0` and seems to extend infinitely toward **positive** `x` and `y`; negative values are **invalid**, as they represent a location outside the building. You are in a small waiting area at `1,1`.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given `x,y` coordinate will be a wall or an open space using a simple system:

 - Find `x*x + 3*x + 2*x*y + y + y*y`.
 - Add the office designer's favorite number (your puzzle input).
 - Find the [binary representation](https://en.wikipedia.org/wiki/Binary_number) of that sum; count the **number** of [bits](https://en.wikipedia.org/wiki/Bit) that are `1`.
   - If the number of bits that are `1` is **even**, it's an **open space**.
   - If the number of bits that are `1` is **odd**, it's a **wall**.

For example, if the office designer's favorite number were `10`, drawing walls as `#` and open spaces as `.`, the corner of the building containing `0,0` would look like this:

```
  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
```

Now, suppose you wanted to reach `7,4`. The shortest route you could take is marked as `O`:

```
  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
```

Thus, reaching `7,4` would take a minimum of `11` steps (starting from your current location, `1,1`).

What is the fewest number of steps required for you to reach `31,39`?

### --- Part Two ---

**How many locations** (distinct `x,y` coordinates, including your starting location) can you reach in at most `50` steps?

### [--- Solution ---](day-13.py)

```Python
# advent of code 2016
# day 13

from collections import defaultdict

class SecretMap:
    def __init__(self, value, destination):
        self.value = value
        self.destination = destination
        self.start = (1, 1)
        self.map = {self.start: '.'}

    def navigateMap(self):
        visited_nodes = set()
        self.distances = defaultdict(lambda: 999999)
        self.distances[self.start] = 0
        queue = [(self.start)]
        while queue:
            x, y = queue.pop(0)
            visited_nodes.add((x, y))
            if (x, y) == self.destination:
                return self.distances[(x, y)]
            else:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= x + dx and 0 <= y + dy and (x + dx, y + dy) not in visited_nodes:
                        if (x + dx, y + dy) not in self.map:
                            bin_value = bin((x + dx) * (x + dx) + 3 * (x + dx) + 2 * (x + dx) * (y + dy) + (y + dy) + (y + dy) * (y + dy) + self.value)[2:]
                            ones = bin_value.count('1')
                            if ones % 2 == 0:
                                self.map[(x + dx, y + dy)] = '.'
                            else:
                                self.map[(x + dx, y + dy)] = '#'
                        if self.map[(x + dx, y + dy)] == '.':
                            self.distances[(x + dx, y + dy)] = min(self.distances[(x + dx, y + dy)], self.distances[(x, y)] + 1)
                            if (x + dx, y + dy) not in queue:
                                queue.append(((x + dx, y + dy)))
    
    def countRange(self):
        return sum([distance <= 50 for distance in self.distances.values()])

def part_1(secretMap):
    print('Part 1:', secretMap.navigateMap())

def part_2(secretMap):
    print('Part 2:', secretMap.countRange())

def main():
    secretMap = SecretMap(1350, (31, 39))
    part_1(secretMap)
    part_2(secretMap)

if __name__ == '__main__':
    main()
```