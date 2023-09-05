def occurence_position(BWT, ch):
    return [i for i, letter in enumerate(BWT) if letter == ch]

def Last_to_First(BWT, i):
    ch = BWT[i]
    occurence = occurence_position(BWT, ch)
    order = occurence.index(i)
    return sorted(BWT).index(ch) + order

def BWMatching(LastColumn, Pattern):
    top = 0
    bottom = len(LastColumn) - 1 
    while top <= bottom:
        if len(Pattern) != 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            last_short = LastColumn[top: bottom + 1]
            if symbol in last_short:
                topindex = last_short.index(symbol) + top
                bottomindex = len(last_short) - last_short[::-1].index(symbol) + top -1
                top = Last_to_First(LastColumn, topindex)
                bottom = Last_to_First(LastColumn, bottomindex)
            else:
                return 0
        else:
            return bottom - top + 1

if __name__ == "__main__":
    BWT = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    patterns = ['CCT', 'CAC', 'GAG', 'CAG', 'ATC']
    # with open('rosalind_ba9l.txt', 'r') as f:
    #     BWT = f.readline().strip()
    #     patterns = f.readline().strip()
    #     patterns = patterns.split()
    #     #print(BWT, patterns)
    for pattern in patterns:
        print(BWMatching(BWT, pattern), end = ' ')
                 
        
        