### [--- Day 1: No Time for a Taxicab ---](https://adventofcode.com/2016/day/1)

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all **fifty stars** by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

You're airdropped near **Easter Bunny Headquarters** in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (`L`) or right (`R`) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the [street grid of the city](https://en.wikipedia.org/wiki/Taxicab_geometry), how far is the shortest path to the destination?

For example:

 - Following `R2, L3` leaves you `2` blocks East and `3` blocks North, or `5` blocks away.
 - `R2, R2, R2` leaves you `2` blocks due South of your starting position, which is `2` blocks away.
 - `R5, L5, R5, R3` leaves you `12` blocks away.

**How many blocks away is Easter Bunny HQ?**

### --- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are `R8, R4, R4, R8`, the first location you visit twice is `4` blocks away, due East.

**How many blocks away is the first location you visit twice?**

### [--- Solution ---](day-01.py)

```Python
# advent of code 2016
# day 1

file = 'input.txt'

class CityMap:
    def __init__(self, instructions):
        self.instructions = instructions
        self.compass = {
            'N': {
                'L': {
                    'direction': 'W',
                    'shift': [-1, 0]
                },
                'R': {
                    'direction': 'E',
                    'shift': [1, 0]
                }
            },
            'E': {
                'L': {
                    'direction': 'N',
                    'shift': [0, 1]
                },
                'R': {
                    'direction': 'S',
                    'shift': [0, -1]
                }
            },
            'S': {
                'L': {
                    'direction': 'E',
                    'shift': [1, 0]
                },
                'R': {
                    'direction': 'W',
                    'shift': [-1, 0]
                }
            },
            'W': {
                'L': {
                    'direction': 'S',
                    'shift': [0, -1]
                },
                'R': {
                    'direction': 'N',
                    'shift': [0, 1]
                }
            }
        }

    def parseInstruction(self, instruction, position, facing):
        turn = instruction[0]
        distance = int(instruction[1:])
        new_position = [x + (y * distance) for x, y in zip(position, self.compass[facing][turn]['shift'])]
        new_facing = self.compass[facing][turn]['direction']
        return [new_facing, new_position]

    def followAllInstructions(self):
        facing = 'N'
        position = [0, 0]
        for instruction in self.instructions:
            facing, position = self.parseInstruction(instruction, position, facing)
        return self.evaluateDistance(position)
    
    def followUntilDuplicate(self):
        facing = 'N'
        position = [0,0]
        history = [[0, 0]]
        for instruction in self.instructions:
            new_facing, new_position = self.parseInstruction(instruction, position, facing)
            old_x, old_y = position
            new_x, new_y = new_position
            x_step = 1 if old_x <= new_x else -1
            y_step = 1 if old_y <= new_y else -1
            for x in range(old_x, new_x + x_step, x_step):
                for y in range(old_y, new_y + y_step, y_step):
                    if [x, y] != position:
                        if [x, y] not in history:
                            history.append([x, y])
                        else:
                            return self.evaluateDistance([x, y])
            position = new_position
            facing = new_facing

    def evaluateDistance(self, position):
        return sum([abs(x) for x in position])
    
def part_1(cityMap):
    print('Part 1:', cityMap.followAllInstructions())

def part_2(cityMap):
    print('Part 2:', cityMap.followUntilDuplicate())

def main():
    instructions = [instruction.strip() for instruction in open(file, 'r').read().split(',')]
    cityMap = CityMap(instructions)
    part_1(cityMap)
    part_2(cityMap)

if __name__ == '__main__':
    main()
```