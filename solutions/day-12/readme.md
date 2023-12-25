### [--- Day 12: Leonardo's Monorail ---](https://adventofcode.com/2016/day/12)

You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some [tiger lilies](https://www.google.com/search?q=tiger+lilies&tbm=isch), you manage to decrypt some of the files you extracted from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the [new computer](https://adventofcode.com/2016/day/11) you just assembled. You'll have to execute the code and get the password.

The assembunny code you've extracted operates on four [registers](https://en.wikipedia.org/wiki/Processor_register) (`a`, `b`, `c`, and `d`) that start at `0` and can hold any [integer](https://en.wikipedia.org/wiki/Integer). However, it seems to make use of only a few [instructions](https://en.wikipedia.org/wiki/Instruction_set):

 - `cpy x y` copies `x` (either an integer or the **value** of a register) into register `y`.
 - `inc x` **increases** the value of register `x` by one.
 - `dec x` **decreases** the value of register `x` by one.
 - `jnz x y` **jumps** to an instruction `y` away (positive means forward; negative means backward), but only if `x` is **not zero**.

The `jnz` instruction moves relative to itself: an offset of `-1` would continue at the previous instruction, while an offset of `2` would **skip over** the next instruction.

For example:

```
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
```

The above code would set register a to `41`, increase its value by `2`, decrease its value by `1`, and then skip the last `dec a` (because a is not zero, so the jnz a `2` skips it), leaving register a at `42`. When you move past the last instruction, the program halts.

After executing the assembunny code in your puzzle input, **what value is left in register `a`?**

### --- Part Two ---

As you head down the fire escape to the monorail, you notice it didn't start; register `c` needs to be initialized to the position of the ignition key.

If you **instead initialize register `c` to be `1`**, what value is now left in register `a`?

### [--- Solution ---](day-12.py)
```Python
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
```