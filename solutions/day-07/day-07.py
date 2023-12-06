class TLSAssessor:
    def __init__(self, ips):
        self.ips = ips

    def containsABBA(self, string):
        return any([string[i] == string[i + 3] and string[i] != string[i + 1] and string[i + 1] == string[i + 2] for i in range(len(string) - 3)])

    def matchesABAtoBAB(self, ip):
        abas = []
        for i in range(len(ip) - 2):
            if ip[i] == ip[i + 2] and ip[i] != ip[i + 1] and '[' not in ip[i:i + 3] and ']' not in ip[i:i + 3]:
                abas.append(ip[i:i + 3])
        for aba in list(set(abas)):
            a, b = [char for char in aba[:2]]
            bab = ''.join([b, a, b])
            safe_aba = re.search('(?:\[.*?\])*[^\[]*(' + aba + ').*', ip)
            safe_bab = re.search('.*?\[.*?(' + bab + ').*\].*', ip)
            if safe_aba  is not None and safe_bab is not None:
                relevant = [char for char in re.sub('[a-z]', '_', ip)]
                print(''.join(relevant))
                print(safe_aba.start())
                relevant[safe_aba.start():safe_aba.end()] = [char for char in aba]
                relevant[safe_bab.start():safe_bab.end()] = [char for char in bab]
                print(''.join(relevant))
                return True
        return False

    def meetsTLS(self, ip):
        abba = self.containsABBA(ip)
        safe_protected_strings = not any([self.containsABBA(segment) for segment in list(re.findall('\[.*?\]', ip))])
        return abba and safe_protected_strings
    
    def meetsSSL(self, ip):
        return self.matchesABAtoBAB(ip)