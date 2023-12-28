# advent of code 2016
# day 18

file = 'input.txt'

class TrapFloor:
    def __init__(self, row_zero):
        self.image = [row_zero]
        self.width = len(row_zero)

    def fillFloor(self, n=40):
        prior_line = [x for x in self.image[0]]
        y = 1
        while y < n:
            new_line = prior_line.copy()
            for x in range(len(prior_line)):
                l, c, r = [(prior_line[x + d] if 0 <= x + d < len(prior_line) else '.') == '^' for d in [-1, 0, 1]]
                new_line[x] = '^' if (l and c and not r) or (c and r and not l) or (l and not r and not c) or (r and not c and not l) else '.'
            if ''.join(new_line) in self.image:
                print('looped!')                
                break
            self.image.append(''.join(new_line))
            prior_line = new_line.copy()
            y += 1
        if y == n:
            return sum([row.count('.') for row in self.image])
        else:
            start = self.image.index(''.join(new_line))
            end = y
            cycle = end - start
            count_per_cycle = sum([self.image[i].count('.') for i in range(start, end)])
            cycles = (n - start) // cycle
            head = sum([self.image[i].count('.') for i in range(start)])
            tail_length = (n - start) % cycle
            tail = sum([self.image[i].count('.') for i in range(start, start + tail_length)])
            return head + count_per_cycle * cycles + tail

    def printMap(self):
        print('\n'.join(self.image))

def part_1(trapFloor):
    print('Part 1:', trapFloor.fillFloor(40))

def part_2(trapFloor):
    print('Part 2:', trapFloor.fillFloor(400000))

def main():
    row_zero = open(file, 'r').read().strip()
    trapFloor = TrapFloor(row_zero)
    part_1(trapFloor)
    part_2(trapFloor)

if __name__ == '__main__':
    main()