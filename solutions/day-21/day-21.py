# advent of code 2016
# day 21

import re

file = 'input.txt'

class Scramble:
    def __init__(self, password, instructions):
        self.password = [x for x in password]
        self.scrambled_password = [x for x in password]
        self.instructions = instructions

    def swapPositions(self, x, y):
        x_val = self.scrambled_password[x]
        y_val = self.scrambled_password[y]
        self.scrambled_password[x] = y_val
        self.scrambled_password[y] = x_val

    def swapLetter(self, x, y):
        x_index = self.scrambled_password.index(x)
        y_index = self.scrambled_password.index(y)
        self.scrambled_password[x_index] = y
        self.scrambled_password[y_index] = x

    def rotatePosition(self, rev, x):
        if rev is False:
            x_index = self.scrambled_password.index(x)
            f = 1 if x_index >= 4 else 0
            self.scrambled_password = self.scrambled_password[-(x_index + 1 + f) % len(self.scrambled_password):] + self.scrambled_password[:-(x_index + 1 +f) % len(self.scrambled_password)]
        else:
            for i in range(len(self.scrambled_password)):
                test = self.scrambled_password[(i + 1) % len(self.scrambled_password):] + self.scrambled_password[:(i + 1) % len(self.scrambled_password)]
                x_index = test.index(x)
                f = 1 if x_index >= 4 else 0
                if (f + x_index) % len(test) == i:
                    self.scrambled_password = test
                    break

    def rotateDirection(self, rev, dir, x):
        if (dir == 'right' and rev is False) or (dir == 'left' and rev is True):
            self.scrambled_password = self.scrambled_password[-x:] + self.scrambled_password[:-x]
        else:
            self.scrambled_password = self.scrambled_password[x:] + self.scrambled_password[:x]

    def reversePositions(self, x, y):
        self.scrambled_password[x:y + 1] = self.scrambled_password[x:y + 1][::-1]

    def move(self, rev, x, y):
        if rev:
            (x, y) = (y, x)
        x_val = self.scrambled_password.pop(x)
        self.scrambled_password.insert(y, x_val)

    def scramblePassword(self, rev=False):
        if rev:
            instructions = self.instructions[::-1]
        else:
            instructions = self.instructions
        for instruction in instructions:
            if 'swap position' in instruction:
                x, y = [int(x) for x in re.findall('\d+', instruction)]
                self.swapPositions(x, y)
            elif 'swap letter' in instruction:
                x, y = re.search('swap letter (\w) with letter (\w)', instruction).groups()
                self.swapLetter(x, y)
            elif 'rotate based' in instruction:
                x = instruction[-1]
                self.rotatePosition(rev, x)
            elif 'rotate' in instruction:
                dir, x = re.search('(left|right)\s(\d+)', instruction).groups()
                self.rotateDirection(rev, dir, int(x))
            elif 'reverse' in instruction:
                x, y = [int(x) for x in re.findall('\d+', instruction)]
                self.reversePositions(x, y)
            else:
                x, y = [int(x) for x in re.findall('\d+', instruction)]
                self.move(rev, x, y)
        return ''.join(self.scrambled_password)

def part_1(instructions):
    print('Part 1:', Scramble('abcdefgh', instructions).scramblePassword())

def part_2(instructions):
    print('Part 2:', Scramble('fbgdceah', instructions).scramblePassword(True))

def main():
    instructions = open(file, 'r').read().splitlines()
    part_1(instructions)
    part_2(instructions)

if __name__ == '__main__':
    main()
