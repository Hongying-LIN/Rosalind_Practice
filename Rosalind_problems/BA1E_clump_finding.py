from find_most_words_v2 import *
#genome = input()
#k = int(input())
#L = int(input())
#t = int(input())
 

def Findclumps(text, k, L, t):
    pattern = []
    n = len(text)
    for i in range(n-L+1):
        window = text[i:i+L]
        freqMap = FrequencyTable(window, k)
        for key in freqMap.keys():
            if freqMap[key] >= t :
               pattern.append(key)
    pattern = list(set(pattern))
    return pattern

if __name__ == "__main__" :
    genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
    k, L, t = 5, 75, 4
    # with open("rosalind_ba1e.txt", "r") as f:
    #     genome = f.readline().strip()
    #     k, L, t = map(int, f.readline().strip().split())
    patternlist = Findclumps(genome, k, L, t)
    print(" ".join(patternlist))
 
