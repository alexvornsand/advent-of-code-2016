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