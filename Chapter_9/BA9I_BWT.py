def Burrows_Wheeler_Transformer(text):
    patterns = []
    for i in range(len(text)):
        patterns.append(text[i:] + text[:i])
    patterns = sorted(patterns)
    BWT = ''.join([str[-1] for str in patterns])
    return BWT

if __name__ == "__main__":
    # text = 'GCGTGCCTGGTCA$'
    with open("rosalind_ba9i.txt", "r") as f:
        text = f.read().strip()
    print(Burrows_Wheeler_Transformer(text))