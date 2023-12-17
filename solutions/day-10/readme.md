### [--- Day 10: Balance Bots ---](https://adventofcode.com/2016/day/10)

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has **two** microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its **lower-value** or **higher-value** chip.

For example, consider the following instructions:

```
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
```

 - Initially, bot `1` starts with a value-`3` chip, and bot `2` starts with a value-`2` chip and a value-`5` chip.
 - Because bot `2` has two microchips, it gives its lower one (`2`) to bot `1` and its higher one (`5`) to bot `0`.
 - Then, bot `1` has two microchips; it puts the value-`2` chip in output `1` and gives the value-`3` chip to bot `0`.
 - Finally, bot `0` has two microchips; it puts the `3` in output `2` and the `5` in output `0`.

In the end, output bin `0` contains a value-`5` microchip, output bin `1` contains a value-`2` microchip, and output bin `2` contains a value-`3` microchip. In this configuration, bot number `2` is responsible for comparing value-`5` microchips with value-`2` microchips.

Based on your instructions, **what is the number of the bot** that is responsible for comparing value-`61` microchips with value-`17` microchips?

### --- Part Two ---

What do you get if you **multiply together the values** of one chip in each of outputs `0`, `1`, and `2`?

### [--- Solution ---](day-10.py)
```Python
# advent of code 2016
# day 10

import re

file = 'input.txt'

class FactoryBots:
    def __init__(self, instructions):
        self.instructions = instructions
        self.data_store = {'bot': {}, 'output': {}}
        self.bot_of_interest = ''

    def pickUpChips(self, chip, bot):
        if bot in self.data_store['bot']:
            self.data_store['bot'][bot].append(chip)
        else:
            self.data_store['bot'][bot] = [chip]

    def distributeChips(self, src, src_id, dest_low, dest_low_id, dest_high, dest_high_id):
        if src_id in self.data_store[src] and len(self.data_store[src][src_id]) == 2:
            low = str(min([int(x) for x in self.data_store[src][src_id]]))
            high = str(max([int(x) for x in self.data_store[src][src_id]]))
            if dest_low_id in self.data_store[dest_low]:
                self.data_store[dest_low][dest_low_id].append(low)
            else:
                self.data_store[dest_low][dest_low_id] = [low]
            if dest_high_id in self.data_store[dest_high]:
                self.data_store[dest_high][dest_high_id].append(high)
            else:
                self.data_store[dest_high][dest_high_id] = [high]
            self.data_store[src][src_id] = []
            if low == '17' and high == '61':
                self.bot_of_interest = src_id
            return 'worked'
        else:
            return 'skip'

    def runInstruction(self, instruction):
        if instruction.split(' ')[0] == 'value':
            chip, bot = list(re.findall('\d+', instruction))
            self.pickUpChips(chip, bot)
            return 'worked'
        else:
            src, src_id, dest_low, dest_low_id, dest_high, dest_high_id = re.search('([a-z]+)\s(\d+).*?([a-z]+)\s(\d+).*?([a-z]+)\s(\d+)', instruction).groups()
            result = self.distributeChips(src, src_id, dest_low, dest_low_id, dest_high, dest_high_id)
            return result
            
    def runInstructions(self):
        while len(self.instructions) > 0:
            instruction = self.instructions[0]
            result = self.runInstruction(instruction) 
            if result == 'worked':
                self.instructions.pop(0)
            elif result == 'skip':
                self.instructions.pop(0)
                self.instructions.append(instruction)

def part_1(factoryBots):
    print('Part 1:', factoryBots.bot_of_interest)

def part_2(factoryBots):
    print('Part 2:', int(factoryBots.data_store['output']['0']) * int(factoryBots.data_store['output']['1']) * int(factoryBots.data_store['output']['2']))

def main():
    instructions = open(file, 'r').read().splitlines()
    factoryBots = FactoryBots(instructions)
    factoryBots.runInstructions()
    part_1(factoryBots)
    part_2(factoryBots)

if __name__ == '__main__':
    main()
```