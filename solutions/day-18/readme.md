### [--- Day 18: Like a Rogue ---](https://adventofcode.com/2016/day/18)

As you enter this room, you hear a loud click! Some of the tiles in the floor here seem to be pressure plates for [traps](https://nethackwiki.com/wiki/Trap), and the trap you just triggered has run out of... whatever it tried to do to you. You doubt you'll be so lucky next time.

Upon closer examination, the traps and safe tiles in this room seem to follow a pattern. The tiles are arranged into rows that are all the same width; you take note of the safe tiles (`.`) and traps (`^`) in the first row (your puzzle input).

The type of tile (trapped or safe) in each row is based on the types of the tiles in the same position, and to either side of that position, in the previous row. (If either side is off either end of the row, it counts as "safe" because there isn't a trap embedded in the wall.)

For example, suppose you know the first row (with tiles marked by letters) and want to determine the next row (with tiles marked by numbers):

```
ABCDE
12345
```

The type of tile `2` is based on the types of tiles `A`, `B`, and `C`; the type of tile `5` is based on tiles `D`, `E`, and an imaginary "safe" tile. Let's call these three tiles from the previous row the **left**, **center**, and **right** tiles, respectively. Then, a new tile is a **trap** only in one of the following situations:

 - Its **left** and **center** tiles are traps, but its **right** tile is not.
 - Its **center** and **right** tiles are traps, but its **left** tile is not.
 - Only its **left** tile is a trap.
 - Only its **right** tile is a trap.

In any other situation, the new tile is safe.

Then, starting with the row `..^^.`, you can determine the next row by applying those rules to each new tile:

 - The leftmost character on the next row considers the left (nonexistent, so we assume "safe"), center (the first `.`, which means "safe"), and right (the second `.`, also "safe") tiles on the previous row. Because all of the trap rules require a trap in at least one of the previous three tiles, the first tile on this new row is also safe, `.`.
 - The second character on the next row considers its left (`.`), center (`.`), and right (`^`) tiles from the previous row. This matches the fourth rule: only the right tile is a trap. Therefore, the next tile in this new row is a trap, `^`.
 - The third character considers `.^^`, which matches the second trap rule: its center and right tiles are traps, but its left tile is not. Therefore, this tile is also a trap, `^`.
 - The last two characters in this new row match the first and third rules, respectively, and so they are both also traps, `^`.

After these steps, we now know the next row of tiles in the room: `.^^^^`. Then, we continue on to the next row, using the same rules, and get `^^..^`. After determining two new rows, our map looks like this:

```
..^^.
.^^^^
^^..^
```

Here's a larger example with ten tiles per row and ten rows:

```
.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^
```

In ten rows, this larger example has `38` safe tiles.

Starting with the map in your puzzle input, in a total of 40 rows (including the starting row), **how many safe tiles** are there?

### --- Part 2 ---

**How many safe tiles** are there in a total of `400000` rows?

### [--- Solution ---](day-18.py)
```Python
# advent of code 2016
# day 18

file = 'input.txt'

class TrapFloor:
    def __init__(self, row_zero):
        self.image = [row_zero]
        self.width = len(row_zero)

    def fillFloor(self, n=40):
        prior_line = [x for x in self.image[0]]
        y = 1
        while y < n:
            new_line = prior_line.copy()
            for x in range(len(prior_line)):
                l, c, r = [(prior_line[x + d] if 0 <= x + d < len(prior_line) else '.') == '^' for d in [-1, 0, 1]]
                new_line[x] = '^' if (l and c and not r) or (c and r and not l) or (l and not r and not c) or (r and not c and not l) else '.'
            if ''.join(new_line) in self.image:
                print('looped!')                
                break
            self.image.append(''.join(new_line))
            prior_line = new_line.copy()
            y += 1
        if y == n:
            return sum([row.count('.') for row in self.image])
        else:
            start = self.image.index(''.join(new_line))
            end = y
            cycle = end - start
            count_per_cycle = sum([self.image[i].count('.') for i in range(start, end)])
            cycles = (n - start) // cycle
            head = sum([self.image[i].count('.') for i in range(start)])
            tail_length = (n - start) % cycle
            tail = sum([self.image[i].count('.') for i in range(start, start + tail_length)])
            return head + count_per_cycle * cycles + tail

    def printMap(self):
        print('\n'.join(self.image))

def part_1(trapFloor):
    print('Part 1:', trapFloor.fillFloor(40))

def part_2(trapFloor):
    print('Part 2:', trapFloor.fillFloor(400000))

def main():
    row_zero = open(file, 'r').read().strip()
    trapFloor = TrapFloor(row_zero)
    part_1(trapFloor)
    part_2(trapFloor)

if __name__ == '__main__':
    main()
```