def reversecomplement(DNAseq):
    complementRule = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join([complementRule[x] for x in reversed(DNAseq)])

if __name__ == "__main__" :
    DNAseq = "AAAACCCGGT"
    #with open("rosalind_ba1c.txt", "r") as f:
    #    DNAseq = f.readline().strip()
    print(reversecomplement(DNAseq))
