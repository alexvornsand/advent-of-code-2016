# advent of code 2016
# day 6

file = 'input.txt'

class Transmission:
    def __init__(self, messages):
        self.messages = messages
        self.columns = {}

    def fillColumns(self):
        for i in range(len(self.messages[0])):
            self.columns[i] = []
        for message in self.messages:
            for i in range(len(message)):
                self.columns[i].append(message[i])

    def evaluateColumn(self, column, method='max'):
        letters = set(column)
        counts = {}
        for letter in letters:
            counts[letter] = column.count(letter)
        if method == 'max':
            return max(counts, key=counts.get)
        else:
            return min(counts, key=counts.get)

    def parseTransmission(self, method='max'):
        return ''.join(self.evaluateColumn(self.columns[column], method) for column in self.columns)

def part_1(transmission):
    print('Part 1:', transmission.parseTransmission())

def part_2(transmission):
    print('Part 2:', transmission.parseTransmission('min'))

def main():
    messages = open(file, 'r').read().splitlines()
    transmission = Transmission(messages)
    transmission.fillColumns()
    part_1(transmission)
    part_2(transmission)

if __name__ == '__main__':
    main()