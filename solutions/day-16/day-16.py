# advent of code 2016
# day 16

class Checksum:
    def __init__(self, base, length):
        self.base = base
        self.length = length

    def buildString(self):
        while len(self.base) < self.length:
            a = self.base
            b = ''.join([str(abs(int(x) - 1)) for x in self.base[::-1]])
            self.base = a + '0' + b
        self.base = self.base[:self.length]
        return self

    def checkSum(self):
        while True:
            if len(self.base) % 2 == 1:
                return self.base
            else:
                self.base = ''.join(['1' if self.base[2 * i] == self.base[2 * i + 1] else '0' for i in range(int(len(self.base) / 2))])

def part_1(number):
    print('Part 1:', Checksum(number, 272).buildString().checkSum())

def part_2(number):
    print('Part 2:', Checksum(number, 35651584).buildString().checkSum())

def main():
    number = '11100010111110100'
    part_1(number)
    part_2(number)

if __name__ == '__main__':
    main()