##Find the Most Frequent Words in a String 
#DNAseq = input()
#k = int(input())

def FrequencyTable(DNAseq, k):
    freqMap = {}
    n = len(DNAseq)
    for i in range(0, n-k+1):
        Pattern = DNAseq[i:i+k]
        if Pattern not in freqMap.keys():
            freqMap[Pattern] = 1
        else:
            freqMap[Pattern] += 1
    return freqMap

if __name__ == "__main__":
    with open ("rosalind_ba1b.txt","r") as f:
        DNAseq = f.readline().strip()
        k = int(f.readline().strip())
    freqMap = FrequencyTable(DNAseq, k)
    max_number = max(freqMap.values())
    for key in freqMap.keys():
        if freqMap[key] == max_number:
            print(key, end=" ")




