# advent of code 2016
# day 8

import numpy as np

file = 'input.txt'

class Display:
    def __init__(self, instructions):
        self.instructions = []
        for instruction in instructions:
            if 'rect' in instruction:
                self.instructions.append(['rect', [int(x) for x in instruction.split(' ')[1].split('x')]])
            elif 'row' in instruction:
                self.instructions.append(['row', [int(x) for x in instruction.split('=')[1].split(' by ')]])
            else:
                self.instructions.append(['column', [int(x) for x in instruction.split('=')[1].split(' by ')]])
        self.display = np.array([[0 for c in range(50)] for r in range(6)])

    def rect(self, a, b):
        self.display[:b, :a] = 1

    def row(self, r, d):
        self.display[r, :] = list(self.display[r, -d:]) + list(self.display[r, :-d])

    def column(self, c, d):
        self.display[:, c] = list(self.display[-d:, c]) + list(self.display[:-d, c])

    def processInstruction(self, instruction):
        process, [x, y] = instruction 
        if process == 'rect':
            self.rect(x, y)
        elif process == 'row':
            self.row(x, y)
        else:
            self.column(x, y)

    def printDisplay(self):
        return '\n'.join(''.join([{1: '#', 0: ' '}[x] for x in row]) for row in self.display)

    def processInstructions(self):
        for instruction in self.instructions:
            self.processInstruction(instruction)

def part_1(display):
    print('Part 1:', sum(sum(display.display)))

def part_2(display):
    print('Part 2:', display.printDisplay(), sep = '\n')

def main():
    instructions = open(file, 'r').read().splitlines()
    display = Display(instructions)
    display.processInstructions()
    part_1(display)
    part_2(display)

if __name__ == '__main__':
    main()