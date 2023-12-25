# advent of code 2016
# day 14

from hashlib import md5
import re

salt = 'ihaygndm'

class Decrypter:
    def __init__(self, salt):
        self.salt = salt
        self.index = 0

    def hash(self, text, n=1):
        strng = text
        for i in range(n):
            strng = md5(bytes(strng, 'utf-8')).hexdigest()
        return strng

    def findHashes(self, n=1):
        self.keys = []
        self.hashes = [self.hash(self.salt + str(i), n) for i in range(1001)]    
        while len(self.keys) < 64:
            trip = re.search('(?P<d>\w)(?P=d)(?P=d)', self.hashes[0])
            self.hashes.pop(0)
            if trip:
                digit = trip.group()[0]
                if any([digit * 5 in hash for hash in self.hashes]):
                    self.keys.append(self.index)
            self.index += 1
            self.hashes.append(self.hash(self.salt + str(self.index + 1000), n))
        return self.keys[-1]
    
def part_1(decrypter):
    print('Part 1:', decrypter.findHashes())

def part_2(decrypter):
    print('Part 2:', decrypter.findHashes(2017))


def main():
    decrypter = Decrypter(salt)
    part_1(decrypter)
    part_2(decrypter)

if __name__ == '__main__':
    main()