#Find all occurrances of a pattern in a string
#pattern = input()
#DNAseq = input()

def patternmatch(pattern, DNAseq):
    n = len(pattern)
    for i in range(len(DNAseq)):
        if DNAseq[i:i+n] == pattern:
            print(i, end=" ")

if __name__ == "__main__":
    #pattern = "ATAT"
    #DNAseq = "GATATATGCATATACTT"
    with open("rosalind_ba1d.txt","r") as f:
        pattern = f.readline().strip()
        DNAseq = f.readline().strip()
    patternmatch(pattern, DNAseq)

