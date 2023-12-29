# advent of code 2016
# day 20

file = 'input.txt'

class Firewall:
    def __init__(self, ranges):
        self.ranges = sorted([tuple([int(x) for x in ip_range.split('-')]) for ip_range in ranges], key=lambda r: r[0])

    def findSmallestGap(self):
        i = 0
        while True:
            range_cap = self.ranges[i][1] + 1
            if self.ranges[i + 1][0] <= range_cap or any([range_cap < self.ranges[j][1] for j in range(i)]):
                i += 1
            else:
                return range_cap
    
    def findNumberOfGaps(self):
        floor = 0
        ceiling = 0
        valid_ranges = []
        for i in range(len(self.ranges)):
            m, n = self.ranges[i]
            if m > ceiling + 1:
                valid_ranges.append([floor, ceiling])
                floor = m
                ceiling = n
            else:
                ceiling = max(ceiling, n)
        valid_ranges.append([floor, ceiling])        
        return 4294967295 + 1 - sum([n - m + 1 for m, n in valid_ranges])
    
def part_1(firewall):
    print('Part 1:', firewall.findSmallestGap())

def part_2(firewall):
    print('Part 2:', firewall.findNumberOfGaps())

def main():
    ranges = open(file, 'r').read().splitlines()
    firewall = Firewall(ranges)
    part_1(firewall)
    part_2(firewall)

if __name__ == '__main__':
    main()
