def occurence_position(BWT, ch):
    return [i for i, letter in enumerate(BWT) if letter == ch]

def Last_to_First(BWT, i):
    ch = BWT[i]
    occurence = occurence_position(BWT, ch)
    order = occurence.index(i)
    return sorted(BWT).index(ch) + order

if __name__ == "__main__":
    # BWT = 'T$GACCA'
    # i = 5
    with open("rosalind_ba9k.txt", "r") as f:
        BWT = f.readline().strip()
        i = int(f.readline())
    print(Last_to_First(BWT, i))