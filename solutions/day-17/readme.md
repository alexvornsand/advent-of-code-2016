### [--- Day 17: Two Steps Forward ---](https://adventofcode.com/2016/day/17)

You're trying to access a secure vault protected by a `4x4` grid of small rooms connected by doors. You start in the top-left room (marked `S`), and you can access the vault (marked `V`) once you reach the bottom-right room:

```
#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |  
####### V
```

Fixed walls are marked with `#`, and doors are marked with `-` or `|`.

The doors in your **current room** are either open or closed (and locked) based on the hexadecimal [MD5](https://en.wikipedia.org/wiki/MD5) hash of a passcode (your puzzle input) followed by a sequence of uppercase characters representing the **path you have taken so far** (`U` for up, `D` for down, `L` for left, and `R` for right).

Only the first four characters of the hash are used; they represent, respectively, the doors **up**, **down**, **left**, and **right** from your current position. Any `b`, `c`, `d`, `e`, or `f` means that the corresponding door is **open**; any other character (any number or `a`) means that the corresponding door is **closed and locked**.

To access the vault, all you need to do is reach the bottom-right room; reaching this room opens the vault and all doors in the maze.

For example, suppose the passcode is `hijkl`. Initially, you have taken no steps, and so your path is empty: you simply find the MD5 hash of `hijkl` alone. The first four characters of this hash are `ced9`, which indicate that up is open (`c`), down is open (`e`), left is open (`d`), and right is closed and locked (`9`). Because you start in the top-left corner, there are no "up" or "left" doors to be open, so your only choice is **down**.

Next, having gone only one step (down, or `D`), you find the hash of `hijklD`. This produces `f2bc`, which indicates that you can go back up, left (but that's a wall), or right. Going right means hashing `hijklDR` to get `5745` - all doors closed and locked. However, going **up** instead is worthwhile: even though it returns you to the room you started in, your path would then be `DU`, opening a **different set of doors**.

After going DU (and then hashing hijklDU to get 528e), only the right door is open; after going DUR, all doors lock. (Fortunately, your actual passcode is not hijkl).

Passcodes actually used by Easter Bunny Vault Security do allow access to the vault if you know the right path. For example:

 - If your passcode were `ihgpwlah`, the shortest path would be `DDRRRD`.
 - With `kglvqrro`, the shortest path would be `DDUDRLRRUDRD`.
 - With `ulqzkmiv`, the shortest would be `DRURDRUDDLLDLUURRDULRLDUUDDDRR`.

Given your vault's passcode, **what is the shortest path** (the actual path, not just the length) to reach the vault?

Your puzzle input is `qzthpkfp`.

### --- Part Two ---

You're curious how robust this security solution really is, and so you decide to find longer and longer paths which still provide access to the vault. You remember that paths always end the first time they reach the bottom-right room (that is, they can never pass through it, only end in it).

For example:

 - If your passcode were `ihgpwlah`, the longest path would take `370` steps.
 - With `kglvqrro`, the longest path would be `492` steps long.
 - With `ulqzkmiv`, the longest path would be `830` steps long.

**What is the length of the longest path** that reaches the vault?

### [--- Solution ---](day-17.py)
```Python
# advent of code 2016
# day 17

from hashlib import md5

class Vaults:
    def __init__(self, password):
        self.password = password

    def findMinPath(self, location, travel_sequence):
        directions = 'UDLR'
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        x, y = location
        if location == (3, 3):
            return travel_sequence
        else:
            next_moves = []
            locks = [x in ['b', 'c', 'd', 'e', 'f'] for x in md5(bytes(self.password + travel_sequence, 'utf-8')).hexdigest()[:4]]
            for neighbor in neighbors:
                dx, dy = neighbor
                if 0 <= x + dx <= 3 and 0 <= y + dy <= 3 and locks[neighbors.index(neighbor)]:
                    next_moves.append([(x + dx, y + dy), travel_sequence + directions[neighbors.index(neighbor)]])
            if len(next_moves) == 0:
                return 'x' * 9999999
            else:
                return min([self.findMinPath(*move) for move in next_moves], key=lambda p: len(p))
            
    def findMaxPath(self, location, travel_sequence):
        directions = 'UDLR'
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        x, y = location
        if location == (3, 3):
            return len(travel_sequence)
        else:
            next_moves = []
            locks = [x in ['b', 'c', 'd', 'e', 'f'] for x in md5(bytes(self.password + travel_sequence, 'utf-8')).hexdigest()[:4]]
            for neighbor in neighbors:
                dx, dy = neighbor
                if 0 <= x + dx <= 3 and 0 <= y + dy <= 3 and locks[neighbors.index(neighbor)]:
                    next_moves.append([(x + dx, y + dy), travel_sequence + directions[neighbors.index(neighbor)]])
            if len(next_moves) == 0:
                return 0
            else:
                return max([self.findMaxPath(*move) for move in next_moves])

def part_1(vaults):
    print('Part 1:', vaults.findMinPath((0, 0), ''))

def part_2(vaults):
    print('Part 2:', vaults.findMaxPath((0, 0), ''))

def main():
    vaults = Vaults('qzthpkfp')
    part_1(vaults)
    part_2(vaults)

if __name__ == '__main__':
    main()
```