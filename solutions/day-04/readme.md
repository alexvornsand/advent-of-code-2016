### [--- Day 4: Security Through Obscurity ---](https://adventofcode.com/2016/day/4#part2)

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

 - `aaaaa-bbb-z-y-x-123[abxyz]` is a real room because the most common letters are `a` (5), `b` (3), and then a tie between `x`, `y`, and `z`, which are listed alphabetically.
 - `a-b-c-d-e-f-g-h-987[abcde]` is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
 - `not-a-real-room-404[oarel]` is a real room.
 - `totally-real-room-200[decoy]` is not.

Of the real rooms from the list above, the sum of their sector IDs is `1514`.

**What is the sum of the sector IDs of the real rooms?**

### --- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art [shift cipher](https://en.wikipedia.org/wiki/Caesar_cipher), which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. `A` becomes `B`, `B` becomes `C`, `Z` becomes `A`, and so on. Dashes become spaces.

For example, the real name for `qzmt-zixmtkozy-ivhz-343` is `very encrypted name`.

**What is the sector ID** of the room where North Pole objects are stored?

### [--- Solution ---](day-04.py)

```Python
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
```