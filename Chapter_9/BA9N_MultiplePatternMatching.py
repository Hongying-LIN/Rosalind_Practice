from BA9I_BWT import BWT
from BA9M_betterBWMatching import betterBWMatching, Create_CountDict, Find_First_Occurance
from BA9G_suffix_array import suffix_array

def MultiplePatternMatch(text, patterns):
    bwt = BWT(text + '$')
    firstColumn = sorted(bwt)
    first_occurance = Find_First_Occurance(firstColumn)
    count_dict = Create_CountDict(bwt)
    Suffix_Array = suffix_array(text + '$')
    all_matched_index = []
    for pattern in patterns:
        top, bottom = betterBWMatching(first_occurance, bwt, pattern, count_dict)
        if not top:
            continue
        matched_index = Suffix_Array[top : bottom + 1]
        all_matched_index += matched_index
    all_matched_index.sort()
    print(' '.join(map(str, all_matched_index)))

if __name__ == '__main__':
    # text = 'AATCGGGTTCAATCGGGGT'
    # patterns = ['ATCG', 'GGGT']
    with open('rosalind_ba9n.txt', 'r') as f:
        lines = f.read().splitlines()
        text = lines[0]
        patterns= []
    for i in range(1, len(lines)):
        patterns.append(lines[i])
    print(text)
    MultiplePatternMatch(text, patterns)