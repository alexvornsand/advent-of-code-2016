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