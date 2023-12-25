# advent of code 2016
# day 12

file = 'input.txt'

class AssemBunny:
    def __init__(self, instructions):
        self.instructions = instructions

    def processInstructions(self, init=0):
        self.registers = {'a': init, 'b': init, 'c': init, 'd': init}
        self.cursor = 0
        while True:
            if self.cursor < len(self.instructions):
                instruction = self.instructions[self.cursor]
                command = instruction.split(' ')[0]
                if command in ['inc', 'dec']:
                    register = instruction.split(' ')[1]
                    if command  == 'inc':
                        self.registers[register] += 1
                        self.cursor += 1
                    else:
                        self.registers[register] -= 1
                        self.cursor += 1
                else:
                    value, register = instruction.split(' ')[1:]
                    if command == 'cpy':
                        if value.isdigit():
                            self.registers[register] = int(value)
                        else:
                            self.registers[register] = self.registers[value]
                        self.cursor += 1
                    else:
                        if value.isdigit() and int(value) != 0:
                            self.cursor += int(register)
                        elif not value.isdigit() and self.registers[value] != 0:
                            self.cursor += int(register)
                        else:
                            self.cursor += 1
            else:
                return self.registers['a']
            
def part_1(assemBunny):
    print('Part 1:', assemBunny.processInstructions())

def part_2(assemBunny):
    print('Part 2:', assemBunny.processInstructions(1))

def main():
    instructions = open(file, 'r').read().splitlines()
    assemBunny = AssemBunny(instructions)
    part_1(assemBunny)
    part_2(assemBunny)

if __name__ == '__main__':
    main()