alphabet = ['A', 'T', 'G', 'C', '$']

def Create_CountDict(LastColumn):
    count_dict = dict()
    for ch in alphabet:
        count_dict[ch] = [0] * (len(LastColumn) + 1)
    for i in range(len(LastColumn)):
        a_acid = LastColumn[i]
        for ch in alphabet:
            if ch == a_acid:
                count_dict[ch][i+1] = count_dict[ch][i] + 1
            else:
                count_dict[ch][i+1] = count_dict[ch][i]  
    return count_dict

def Find_First_Occurance(LastColumn):
    first_occurance = dict()
    for i, symbol in enumerate(sorted(LastColumn)):
        if symbol not in first_occurance.keys():
            first_occurance[symbol] = i
    return first_occurance

def betterBWMatching(first_occurance,LastColumn, pattern, countdict):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in LastColumn[top : bottom + 1]:
                top = first_occurance[symbol] + countdict[symbol][top]
                bottom =first_occurance[symbol] + countdict[symbol][bottom + 1] - 1
            else:
                return False, False
        else:
            return top, bottom

if __name__ == "__main__":
    # BWT = 'GGCGCCGC$TAGTCACACACGCCGTA'
    # patterns = ['ACC', 'CCG', 'CAG']
    with open('rosalind_ba9m.txt', 'r') as f:
        BWT = f.readline().strip()
        patterns = f.readline().strip()
        patterns = patterns.split() 
    # print(BWT, patterns)
    first_occurance = Find_First_Occurance(BWT)
    count_dict = Create_CountDict(BWT)
    for pattern in patterns:
        print(betterBWMatching(first_occurance, BWT, pattern, count_dict), end = ' ')
    
 
 

 