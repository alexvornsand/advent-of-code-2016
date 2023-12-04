# advent of code 2016
# day 4

import re

file = 'input.txt'

class Room:
    def __init__(self, room_code):
        self.name, self.id, self.check = re.match('([a-z\-]*)\-(\d+)\[([a-z]{5})\]', room_code).groups()
        self.id = int(self.id)
        letters = set([chr for chr in self.name.replace('-', '')])
        counts = {}
        for letter in letters:
            count = self.name.count(letter)
            if count in counts:
                counts[count].append(letter)
            else:
                counts[count] = [letter]
        sorted_letters = [chr for count in sorted(list(counts.keys()))[::-1] for chr in sorted(counts[count])]
        if ''.join(sorted_letters[:5]) == self.check:
            self.valid_room = True
        else:
            self.valid_room = False
        self.decrypted_name = ''.join([chr((ord(char) - ord('a') + self.id) % 26 + ord('a')) if char != '-' else ' ' for char in self.name]) if self.valid_room else ''

class Directory:
    def __init__(self, room_codes):
        self.rooms = [Room(room_code) for room_code in room_codes]

    def totalValidRoomIds(self):
        return sum([room.id for room in self.rooms if room.valid_room])
    
    def findRoom(self, decrypted_name):
        rooms = [room.id for room in self.rooms if room.decrypted_name == decrypted_name]
        if len(rooms) == 0:
            return 'None'
        elif len(rooms) == 1:
            return rooms[0]
        else:
            return rooms
        
def part_1(directory):
    print('Part 1:', directory.totalValidRoomIds())

def part_2(directory):
    print('Part 2:', directory.findRoom('northpole object storage'))

def main():
    rooms = open(file, 'r').read().splitlines()
    directory = Directory(rooms)
    part_1(directory)
    part_2(directory)

if __name__ == '__main__':
    main()