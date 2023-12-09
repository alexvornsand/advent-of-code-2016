# advent of code 2016
# day 9

import re

file = 'input.txt'

class CompressedFile:
    def __init__(self, compressed_file):
        self.compressed_file = compressed_file

    def scoreString(self, string, nesting=False):
        if len(string) == 0:
            return 0
        raw_string = re.search('^[^\(]+', string)
        if raw_string is not None:
            section_score = len(raw_string.group())
            remaining_string = string[section_score:]
            subsequent_score = self.scoreString(remaining_string, nesting)
            return section_score + subsequent_score
        else:            
            multiplication, length, times = re.search('(^\((\d+)x(\d+)\))', string).groups()
            if nesting:
                section_score = int(times) * self.scoreString(string[len(multiplication):len(multiplication) + int(length)], nesting)
                remaining_string = string[len(multiplication) + int(length):]
                subsequent_score = self.scoreString(remaining_string, nesting)
                return section_score + subsequent_score
            else:
                section_score = int(length) * int(times)
                remaining_string = string[len(multiplication) + int(length):]
                subsequent_score = self.scoreString(remaining_string, nesting)
                return section_score + subsequent_score

    def decompressFile(self, nesting=False):
        return self.scoreString(self.compressed_file, nesting)
        
def part_1(compressedFile):
    print('Part 1:', compressedFile.decompressFile())

def part_2(compressedFile):
    print('Part 2:', compressedFile.decompressFile(nesting=True))

def main():
    compressed_file = open(file, 'r').read().strip()
    compressedFile = CompressedFile(compressed_file)
    part_1(compressedFile)
    part_2(compressedFile)

if __name__ == '__main__':
    main()
