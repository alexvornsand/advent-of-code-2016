# advent of code 2016
# day 13

from collections import defaultdict

class SecretMap:
    def __init__(self, value, destination):
        self.value = value
        self.destination = destination
        self.start = (1, 1)
        self.map = {self.start: '.'}

    def navigateMap(self):
        visited_nodes = set()
        self.distances = defaultdict(lambda: 999999)
        self.distances[self.start] = 0
        queue = [(self.start)]
        while queue:
            x, y = queue.pop(0)
            visited_nodes.add((x, y))
            if (x, y) == self.destination:
                return self.distances[(x, y)]
            else:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= x + dx and 0 <= y + dy and (x + dx, y + dy) not in visited_nodes:
                        if (x + dx, y + dy) not in self.map:
                            bin_value = bin((x + dx) * (x + dx) + 3 * (x + dx) + 2 * (x + dx) * (y + dy) + (y + dy) + (y + dy) * (y + dy) + self.value)[2:]
                            ones = bin_value.count('1')
                            if ones % 2 == 0:
                                self.map[(x + dx, y + dy)] = '.'
                            else:
                                self.map[(x + dx, y + dy)] = '#'
                        if self.map[(x + dx, y + dy)] == '.':
                            self.distances[(x + dx, y + dy)] = min(self.distances[(x + dx, y + dy)], self.distances[(x, y)] + 1)
                            if (x + dx, y + dy) not in queue:
                                queue.append(((x + dx, y + dy)))
    
    def countRange(self):
        return sum([distance <= 50 for distance in self.distances.values()])

def part_1(secretMap):
    print('Part 1:', secretMap.navigateMap())

def part_2(secretMap):
    print('Part 2:', secretMap.countRange())

def main():
    secretMap = SecretMap(1350, (31, 39))
    part_1(secretMap)
    part_2(secretMap)

if __name__ == '__main__':
    main()
