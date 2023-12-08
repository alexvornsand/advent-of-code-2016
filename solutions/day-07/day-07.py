# advent of code 2016
# day 7

import re

file = 'input.txt'

class TLSAssessor:
    def __init__(self, ips):
        self.ips = ips

    def meetsTLS(self, ip):
        abba = re.search('(?P<a>\w)(?!(?P=a))(?P<b>\w)(?P=b)(?P=a)', ip) is not None
        br_abba_br = re.search('\[[^\[\]]*(?P<a>\w)(?!(?P=a))(?P<b>\w)(?P=b)(?P=a)', ip) is None
        return abba and br_abba_br

    def meetsSSL(self, ip):
        return re.search('(?P<a>\w)(?!(?P=a))(?P<b>\w)(?P=a)[^\[\]]*(?=(?P<bracket>[\[\]])).*(?P=bracket)[^\[\]]*(?P=b)(?P=a)(?P=b)', ip) is not None
    
def part_1(tlsAssessor):
    print('Part 1:', sum(tlsAssessor.meetsTLS(ip) for ip in tlsAssessor.ips))

def part_2(tlsAssessor):
    print('Part 2:', sum(tlsAssessor.meetsSSL(ip) for ip in tlsAssessor.ips))

def main():
    ips = open(file, 'r').read().splitlines()
    tlsAssessor = TLSAssessor(ips)
    part_1(tlsAssessor)
    part_2(tlsAssessor)    

if __name__ == '__main__':
    main()