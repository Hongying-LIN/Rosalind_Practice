#DNAseq = input()
#pattern = input()

def patterncount(text, pattern):
    count = 0
    for nuc in range(len(text)-len(pattern)+1):
        if text[nuc : nuc+len(pattern)] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    DNAseq = "GCGCG"
    pattern = "GCG"
    #with open("rosalind_ba1a.txt", "r") as f:
    #     text = f.readline().strip()
    #     pattern = f.readline().strip()
    print(patterncount(DNAseq,pattern))