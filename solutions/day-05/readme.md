### [--- Day 5: How About a Nice Game of Chess? ---](https://adventofcode.com/2016/day/5)

You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching [hacking movies](https://en.wikipedia.org/wiki/Hackers_(film)).

The **eight-character password** for the door is generated one character at a time by finding the [MD5](https://en.wikipedia.org/wiki/MD5) hash of some Door ID (your puzzle input) and an increasing integer index (starting with `0`).

A hash indicates the **next character** in the password if its [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) representation starts with **five zeroes**. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is `abc`:

 - The first index which produces a hash that starts with five zeroes is `3231929`, which we find by hashing `abc3231929`; the sixth character of the hash, and thus the first character of the password, is `1`.
 - `5017308` produces the next interesting hash, which starts with `000008f82...`, so the second character of the password is `8`.
 - The third time a hash starts with five zeroes is for `abc5278568`, discovering the character `f`.

In this example, after continuing this search a total of eight times, the password is `18f47a30`.

**Given the actual Door ID, what is the password?**

### --- Part Two ---

As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted **in order**?!), the Easter Bunny engineers have worked out [a better solution](https://www.youtube.com/watch?v=NHWjlCaIrQo&t=25).

Instead of simply filling in the password from left to right, the hash now also indicates the **position** within the password to fill. You still look for hashes that begin with five zeroes; however, now, the **sixth** character represents the **position** (`0`-`7`), and the **seventh** character is the character to put in that position.

A hash result of `000001f` means that `f` is the **second** character in the password. Use only the **first result** for each position, and ignore invalid positions.

For example, if the Door ID is `abc`:

 - The first interesting hash is from `abc3231929`, which produces `0000015...`; so, `5` goes in position `1`: `_5______`.
 - In the previous method, `5017308` produced an interesting hash; however, it is ignored, because it specifies an invalid position (`8`).
 - The second interesting hash is at index `5357525`, which produces `000004e...`; so, `e` goes in position `4`: `_5__e___`.

You almost choke on your popcorn as the final character falls into place, producing the password `05ace8e3`.

Given the actual Door ID and this new method, **what is the password**? Be extra proud of your solution if it uses a cinematic "decrypting" animation.

### [--- Solution ---](day-05.py)

```Python
# advent of code 2016
# day 5

from hashlib import md5

id = 'cxdnnyjw'

class Decryption:
    def __init__(self, id):
        self.id = id
        self.hashes = []
        self.simple_password = ''
        self.complex_password = ''
        self.i = 0

    def findHash(self):
        while True:
            hash = md5(bytes(id + str(self.i), 'utf-8')).hexdigest()
            self.i += 1
            if hash[:5] == '00000':
                return hash

    def findPasswords(self):
        simple = {}
        complex = {}
        while len(simple) < 8 or len(complex) < 8:
            hash = self.findHash()
            if len(simple) < 8:
                simple[len(simple)] = hash[5]
            if hash[5].isdigit() and int(hash[5]) < 8 and hash[5] not in complex:
                complex[hash[5]] = hash[6]
        self.simple_password = ''.join([simple[key] for key in sorted(simple.keys())])
        self.complex_password = ''.join([complex[key] for key in sorted(complex.keys())])

def part_1(decryption):
    print('Part 1:', decryption.simple_password)

def part_2(decryption):
    print('Part 2:', decryption.complex_password)

def main():
    decryption = Decryption(id)
    decryption.findPasswords()
    part_1(decryption)
    part_2(decryption)

if __name__ == '__main__':
    main()
```