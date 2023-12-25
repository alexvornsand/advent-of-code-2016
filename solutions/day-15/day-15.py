# advent of code 2016
# day 15

import re

file = 'input.txt'

class Sculpture:
    def __init__(self, disks):
        self.disks = {int(i): {'n': int(n), 'b': int(b)} for i, n, t, b in [re.findall('\d+', disk) for disk in disks]}

    def findGap(self):
        t = 0
        while True:
            if all([(t + i + self.disks[i]['b']) % self.disks[i]['n'] == 0 for i in self.disks]):
                self.cycle = t
                return t
            else:
                t += 1

    def addDisk(self, n=11, b=0):
        last_disk = max(self.disks)
        self.disks[last_disk + 1] = {'n': n, 'b': b}
        return self.findGap()
    
def part_1(sculpture):
    print('Part 1:', sculpture.findGap())

def part_2(sculpture):
    print('Part 2:', sculpture.addDisk())


def main():
    disks = open(file, 'r').read().splitlines()
    sculpture = Sculpture(disks)
    part_1(sculpture)
    part_2(sculpture)

if __name__ == '__main__':
    main()