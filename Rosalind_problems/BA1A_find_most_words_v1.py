##Find the Most Frequent Words in a String 
DNAseq = input()
k = int(input())

#patterncount is used to count the occurrance number of k-mer pattern
def patterncount(text, pattern):
    count = 0
    for nuc in range(len(text)-len(pattern)+1):
        if text[nuc : nuc+len(pattern)] == pattern:
            count += 1
    return count


# obtain the index of all the max number in the list
def max_index(lst_int):
    index = []
    max_lst=max(lst_int)
    for i in range(len(lst_int)):
        if lst_int[i] == max_lst:
            index.append(i)
    return index 

# obtain all the possible patterns and their number of occurrances
patternlist = []
patternnumber = []
for i in range(len(DNAseq) - k):
    pattern = DNAseq[i:i+k]
    if pattern not in patternlist:
        patternlist.append(pattern)
        patternnumber.append(patterncount(DNAseq,DNAseq[i:i+k]))      

max_patternindex = max_index(patternnumber)

#output the most strings
for i in range(len(max_patternindex)):
    print(patternlist[max_patternindex[i]], end=' ')


    




