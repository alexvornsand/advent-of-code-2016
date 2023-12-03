# advent of code 2016
# day 2

file = 'input.txt'

class Password():
    def __init__(self, instructions):
        self.instructions = instructions

    def nextPosition(self, position, move):
        x, y = position
        if move == 'U':
            y -= 1
        elif move == 'D':
            y += 1
        elif move == 'L':
            x -= 1
        else:
            x += 1
        return [x, y]
    
    def getStartPosition(self, keypad):
        for r in range(len(keypad)):
            for c in range(len(keypad[r])):
                if keypad[r][c] == '5':
                    return [c, r]
    
    def getCode(self, keypad):
        position = self.getStartPosition(keypad)
        code = []
        for line in self.instructions:
            for instruction in line:
                next_position = self.nextPosition(position, instruction)
                if keypad[next_position[1]][next_position[0]] != ' ':
                    position = next_position
            code.append(keypad[position[1]][position[0]])
        return ''.join(code)
    
def part_1(password):
    keypad = [
        [' ', ' ', ' ', ' ', ' '], 
        [' ', '1', '2', '3', ' '], 
        [' ', '4', '5', '6', ' '], 
        [' ', '7', '8', '9', ' '], 
        [' ', ' ', ' ', ' ', ' ']
    ]
    print('Part 1:', password.getCode(keypad))

def part_2(password):
    keypad = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' '],
        [' ', ' ', '2', '3', '4', ' ', ' '],
        [' ', '5', '6', '7', '8', '9', ' '],
        [' ', ' ', 'A', 'B', 'C', ' ', ' '],
        [' ', ' ', ' ', 'D', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    print('Part 2:', password.getCode(keypad))

def main():
    instructions = [[move for move in line] for line in open(file, 'r').read().splitlines()]
    password = Password(instructions)
    part_1(password)
    part_2(password)

if __name__ == '__main__':
    main()
