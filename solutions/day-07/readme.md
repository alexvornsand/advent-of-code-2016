### [--- Day 7: Internet Protocol Version 7 ---](https://adventofcode.com/2016/day/7)

While snooping around the local network of EBHQ, you compile a list of [IP addresses](https://en.wikipedia.org/wiki/IP_address) (they're IPv7, of course; [IPv6](https://en.wikipedia.org/wiki/IPv6) is much too limited). You'd like to figure out which IPs support **TLS** (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or **ABBA**. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as `xyyx` or `abba`. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by **square brackets**.

For example:

 - `abba[mnop]qrst` supports TLS (`abba` outside square brackets).
 - `abcd[bddb]xyyx` does **not** support TLS (`bddb` is within square brackets, even though `xyyx` is outside square brackets).
 - `aaaa[qwer]tyui` does not support TLS (`aaaa` is invalid; the interior characters must be different).
 - `ioxxoj[asdfgh]zxcvbn` supports TLS (`oxxo` is outside square brackets, even though it's within a larger string).

**How many IPs** in your puzzle input support TLS?

### --- Part Two ---

You would also like to know which IPs support **SSL** (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or **ABA**, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or **BAB**, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as `xyx` or `aba`. A corresponding BAB is the same characters but in reversed positions: `yxy` and `bab`, respectively.

For example:

 - `aba[bab]xyz` supports SSL (`aba` outside square brackets with corresponding `bab` within square brackets).
 - `xyx[xyx]xyx` does **not** support SSL (`xyx`, but no corresponding `yxy`).
 - `aaa[kek]eke` supports SSL (`eke` in supernet with corresponding `kek` in hypernet; the `aaa` sequence is not related, because the interior character must be different).
 - `zazbz[bzb]cdb` supports SSL (`zaz` has no corresponding `aza`, but `zbz` has a corresponding `bzb`, even though `zaz` and `zbz` overlap).

**How many IPs** in your puzzle input support SSL?

### [--- Solution ---](day-07.py)

```Python
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
```