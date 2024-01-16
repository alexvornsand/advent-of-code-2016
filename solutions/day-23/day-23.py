# advent of code 2016
# day 23

file = 'Input.txt'

class AssemBunny:
    def __init__(self, instructions):
        self.original_instructions = instructions

    def processInstructions(self, init=0):
        self.instructions = self.original_instructions.copy()      
        self.registers = {'a': init, 'b': init, 'c': init, 'd': init}
        self.cursor = 0
        while self.cursor < len(self.instructions):
            instruction = self.instructions[self.cursor]
            command = instruction.split(' ')[0]
            if command in ['inc', 'dec']:
                register = instruction.split(' ')[1]
                if register in self.registers:
                    if command  == 'inc':
                        self.registers[register] += 1
                        self.cursor += 1
                    else:
                        self.registers[register] -= 1
                        self.cursor += 1
                else:
                    self.cursor += 1
            elif command in ['cpy', 'jnz']:
                value, register = instruction.split(' ')[1:]
                value = int(value) if value.lstrip('-').isdigit() else self.registers[value]
                if command == 'cpy':
                    if register in self.registers:
                        self.registers[register] = value
                    self.cursor += 1
                else:
                    shift = int(register) if register.lstrip('-').isdigit() else self.registers[register]
                    if value == 0:
                        self.cursor += 1
                    else:
                        self.cursor += shift
            else:
                x = self.instructions[self.cursor].split(' ')[1]
                if x.lstrip('-').isdigit():
                    j = int(x)
                else:
                    j = self.registers[x]
                if self.cursor + j < len(self.instructions):
                    target_instruction = self.instructions[self.cursor + j]
                    target_command = target_instruction.split(' ')[0]
                    if target_command in ['inc', 'dec', 'tgl']:
                        register = target_instruction.split(' ')[1]
                        if target_command  == 'inc':
                            self.instructions[self.cursor + j] = ' '.join(['dec', register])
                        else:
                            self.instructions[self.cursor + j] = ' '.join(['inc', register])
                    elif target_command in ['cpy', 'jnz']:
                        value, register = target_instruction.split(' ')[1:]
                        if target_command == 'jnz':
                            self.instructions[self.cursor + j] = ' '.join(['cpy', value, register])
                        else:
                            self.instructions[self.cursor + j] = ' '.join(['jnz', value, register])
                self.cursor += 1
        return self.registers['a']
    
def part_1(assemBunny):
    print('Part 1:', assemBunny.processInstructions(7))

def part_2(assemBunny):
    print('Part 2:', assemBunny.processInstructions(12))


def main():
    instructions = open(file, 'r').read().splitlines()
    assemBunny = AssemBunny(instructions)
    part_1(assemBunny)
    part_2(assemBunny)

if __name__ == '__main__':
    main()