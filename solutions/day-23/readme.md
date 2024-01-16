### [--- Day 23: Safe Cracking ---](https://adventofcode.com/2016/day/23)

This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who **wouldn't** hide a star in a safe behind a painting?

The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see `7`.

When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your [prototype computer](https://adventofcode.com/2016/day/11)! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.

Now, you just need to figure out what output the keypad would have sent to the safe. You extract the [assembunny](https://adventofcode.com/2016/day/12) code from the logic chip (your puzzle input).
The code looks like it uses almost the same architecture and instruction set that the monorail computer used! You should be able to **use the same assembunny interpreter** for this as you did there, but with one new instruction:

`tgl x` **toggles** the instruction `x` away (pointing at instructions like `jnz` does: positive means forward; negative means backward):

 - For **one-argument** instructions, `inc` becomes `dec`, and all other one-argument instructions become `inc`.
 - For **two-argument** instructions, `jnz` becomes `cpy`, and all other two-instructions become `jnz`.
 - The arguments of a toggled instruction are **not affected**.
 - If an attempt is made to toggle an instruction outside the program, **nothing happens**.
 - If toggling produces an **invalid instruction** (like `cpy 1 2`) and an attempt is later made to execute that instruction, **skip it instead**.
 - If `tgl` toggles **itself** (for example, if `a` is `0`, `tgl` a would target itself and become `inc a`), the resulting instruction is not executed until the next time it is reached.

For example, given this program:

```
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
```

 - `cpy 2` a initializes register `a` to `2`.
 - The first `tgl a` toggles an instruction `a` (`2`) away from it, which changes the third `tgl a` into `inc a`.
 - The second `tgl a` also modifies an instruction `2` away from it, which changes the `cpy 1 a` into `jnz 1 a`.
 - The fourth line, which is now `inc a`, increments `a` to `3`.
 - Finally, the fifth line, which is now `jnz 1 a`, jumps `a` (`3`) instructions ahead, skipping the `dec a` instructions.
 - In this example, the final value in register `a` is `3`.

The rest of the electronics seem to place the keypad entry (the number of eggs, `7`) in register `a`, run the code, and then send the value left in register `a` to the safe.

**What value** should be sent to the safe?

### --- Part 2 ---

The safe doesn't open, but it **does** make several angry noises to express its frustration.

You're quite sure your logic is working correctly, so the only other thing is... you check the painting again. As it turns out, colored eggs are still eggs. Now you count `12`.

As you run the program with this new input, the prototype computer begins to **overheat**. You wonder what's taking so long, and whether the lack of any instruction more powerful than "add one" has anything to do with it. Don't bunnies usually **multiply**?

Anyway, **what value** should actually be sent to the safe?

### [--- Solution ---](day-23.py)
```Python
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
```