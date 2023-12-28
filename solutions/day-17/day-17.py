# advent of code 2016
# day 17

from hashlib import md5

class Vaults:
    def __init__(self, password):
        self.password = password

    def findMinPath(self, location, travel_sequence):
        directions = 'UDLR'
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        x, y = location
        if location == (3, 3):
            return travel_sequence
        else:
            next_moves = []
            locks = [x in ['b', 'c', 'd', 'e', 'f'] for x in md5(bytes(self.password + travel_sequence, 'utf-8')).hexdigest()[:4]]
            for neighbor in neighbors:
                dx, dy = neighbor
                if 0 <= x + dx <= 3 and 0 <= y + dy <= 3 and locks[neighbors.index(neighbor)]:
                    next_moves.append([(x + dx, y + dy), travel_sequence + directions[neighbors.index(neighbor)]])
            if len(next_moves) == 0:
                return 'x' * 9999999
            else:
                return min([self.findMinPath(*move) for move in next_moves], key=lambda p: len(p))
            
    def findMaxPath(self, location, travel_sequence):
        directions = 'UDLR'
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        x, y = location
        if location == (3, 3):
            return len(travel_sequence)
        else:
            next_moves = []
            locks = [x in ['b', 'c', 'd', 'e', 'f'] for x in md5(bytes(self.password + travel_sequence, 'utf-8')).hexdigest()[:4]]
            for neighbor in neighbors:
                dx, dy = neighbor
                if 0 <= x + dx <= 3 and 0 <= y + dy <= 3 and locks[neighbors.index(neighbor)]:
                    next_moves.append([(x + dx, y + dy), travel_sequence + directions[neighbors.index(neighbor)]])
            if len(next_moves) == 0:
                return 0
            else:
                return max([self.findMaxPath(*move) for move in next_moves])

def part_1(vaults):
    print('Part 1:', vaults.findMinPath((0, 0), ''))

def part_2(vaults):
    print('Part 2:', vaults.findMaxPath((0, 0), ''))

def main():
    vaults = Vaults('qzthpkfp')
    part_1(vaults)
    part_2(vaults)

if __name__ == '__main__':
    main()