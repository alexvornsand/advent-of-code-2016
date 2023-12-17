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
    print('Part 2:', int(factoryBots.data_store['output']['0'][0]) * int(factoryBots.data_store['output']['1'][0]) * int(factoryBots.data_store['output']['2'][0]))

def main():
    instructions = open(file, 'r').read().splitlines()
    factoryBots = FactoryBots(instructions)
    factoryBots.runInstructions()
    part_1(factoryBots)
    part_2(factoryBots)

if __name__ == '__main__':
    main()