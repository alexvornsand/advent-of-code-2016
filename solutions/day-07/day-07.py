class TLSAssessor:
    def __init__(self, ips):
        self.ips = ips

    def containsABBA(self, string):
        relevant_string = ['_' for i in range(len(string))]
        valid_string = False
        for i in range(len(string) - 3):
            if string[i] in ['[', ']']:
                relevant_string[i] = string[i]
            if string[i] == string[i + 3] and string[i] != string[i + 1] and string[i + 1] == string[i + 2]:
                relevant_string[i:i + 4] = string[i:i + 4]
                valid_string = True
        if valid_string:
            print(''.join(relevant_string))
        return valid_string
#        return any([string[i] == string[i + 3] and string[i] != string[i + 1] and string[i + 1] == string[i + 2] for i in range(len(string) - 3)])
    
    def meetsTLS(self, ip):
        print(ip)
        abba = self.containsABBA(ip)
        abba_in_protected_strings = []
        for protected_string in list(re.findall('\[.*?\]', ip)):
            print(protected_string)
            abba_in_protected_strings.append(self.containsABBA(protected_string))
        safe_protected_strings = not any(abba_in_protected_strings)
#        safe_protected_strings = not any([self.containsABBA(segment) for segment in list(re.findall('\[.*\]?', ip))])
        print(abba, safe_protected_strings)
        print('\n')
        return abba and safe_protected_strings